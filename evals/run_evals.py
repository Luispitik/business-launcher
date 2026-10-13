"""Behaviour evals for Business Launcher, run against the real Claude Code CLI.

Each case in evals/cases/<id>/ has case.json (prompt, optional fixture, must / must_not regexes)
and malo.txt, a known-bad answer. The grader must reject every malo.txt before any real result
is trusted (canary). Each case runs in a fresh temporary folder with the skill copied to
.claude/skills/business-launcher, so only this copy of the skill can load.

Usage: python evals/run_evals.py [--skill-dir DIR] [--model claude-opus-5-5] [--only id,id] [--out DIR]
"""
import argparse, json, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP = {'.git', 'evals', 'scripts', 'dist', '.claude-plugin', 'business-launcher'}


def grade(text, case):
    fails = [f'falta: {p}' for p in case.get('must', []) if not re.search(p, text)]
    fails += [f'prohibido: {p}' for p in case.get('must_not', []) if re.search(p, text)]
    return fails


def install_skill(skill_dir, work):
    dest = work / '.claude' / 'skills' / 'business-launcher'
    dest.mkdir(parents=True)
    for item in skill_dir.iterdir():
        if item.name in SKIP:
            continue
        (shutil.copytree if item.is_dir() else shutil.copy2)(item, dest / item.name)


def run_case(case_dir, case, skill_dir, model, timeout):
    claude = shutil.which('claude')
    if not claude:
        sys.exit('No encuentro el CLI "claude" en el PATH.')
    with tempfile.TemporaryDirectory(prefix='bl-eval-') as tmp:
        work = pathlib.Path(tmp)
        install_skill(skill_dir, work)
        if case.get('fixture'):
            shutil.copytree(case_dir / case['fixture'], work, dirs_exist_ok=True)
        proc = subprocess.run([claude, '-p', case['prompt'], '--model', model],
                              cwd=work, capture_output=True, text=True, encoding='utf-8', timeout=timeout)
        return proc.stdout, proc.stderr, proc.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--skill-dir', default=str(ROOT))
    ap.add_argument('--model', default='claude-opus-5-5')
    ap.add_argument('--only', default='')
    ap.add_argument('--out', default=str(ROOT / 'evals' / 'results'))
    ap.add_argument('--timeout', type=int, default=900)
    ap.add_argument('--grade-only', default='', help='grade existing <id>.txt answers in this folder instead of running the CLI')
    a = ap.parse_args()
    skill_dir = pathlib.Path(a.skill_dir).resolve()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    cases = sorted(p for p in (ROOT / 'evals' / 'cases').iterdir() if (p / 'case.json').exists())
    if a.only:
        wanted = set(a.only.split(','))
        cases = [c for c in cases if c.name in wanted]

    # Canary: every known-bad answer must fail its grader, or no result is trusted.
    for c in cases:
        case = json.loads((c / 'case.json').read_text(encoding='utf-8'))
        if not grade((c / 'malo.txt').read_text(encoding='utf-8'), case):
            sys.exit(f'CANARIO FALLIDO: el comprobador de {c.name} acepta una respuesta mala conocida.')
    print(f'Canarios: {len(cases)} respuestas malas rechazadas.')

    results = []
    for c in cases:
        case = json.loads((c / 'case.json').read_text(encoding='utf-8'))
        print(f'-> {case["id"]} ...', flush=True)
        if a.grade_only:
            answer = pathlib.Path(a.grade_only) / f'{case["id"]}.txt'
            if not answer.exists():
                print('   sin respuesta: no se evalúa'); continue
            stdout, stderr, code = answer.read_text(encoding='utf-8'), '', 0
        else:
            stdout, stderr, code = run_case(c, case, skill_dir, a.model, a.timeout)
        fails = grade(stdout, case) if code == 0 and stdout.strip() else [f'el CLI terminó con código {code}: {(stderr or stdout)[-400:]}']
        if not a.grade_only:
            (out / f'{case["id"]}.txt').write_text(stdout, encoding='utf-8')
        results.append({'id': case['id'], 'ok': not fails, 'fallos': fails, 'proposito': case['proposito']})
        print(f'   {"OK" if not fails else "FALLA"} {fails}')
    (out / 'resultados.json').write_text(json.dumps({'skill_dir': str(skill_dir), 'model': a.model, 'casos': results},
                                                    ensure_ascii=False, indent=1), encoding='utf-8')
    passed = sum(r['ok'] for r in results)
    print(f'{passed}/{len(results)} casos superados. Salidas en {out}')
    sys.exit(0 if passed == len(results) else 1)


if __name__ == '__main__':
    main()
