"""Checks SKILL.md frontmatter against the Agent Skills spec (allowed keys and length limits)
and that every file path the skill mentions exists. Usage: python scripts/validate_skill.py [SKILL_DIR]"""
import pathlib, re, sys
ALLOWED = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
def check(d):
    d = pathlib.Path(d).resolve(); errs = []
    text = (d / 'SKILL.md').read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m: return ['SKILL.md sin frontmatter']
    fm = m.group(1)
    keys = re.findall(r'^([A-Za-z_-]+):', fm, re.M)
    errs += [f'clave no admitida: {k}' for k in keys if k not in ALLOWED]
    name = re.search(r'^name:\s*(\S+)', fm, re.M)
    if not name or not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name.group(1)) or len(name.group(1)) > 64: errs.append('name inválido')
    elif name.group(1) != d.name and d.name != 'business-launcher-src': errs.append(f'la carpeta ({d.name}) no coincide con name ({name.group(1)})')
    desc = re.search(r'^description:\s*>-?\n((?:  .*\n?)+)', fm, re.M)
    dtext = ' '.join(l.strip() for l in desc.group(1).splitlines()) if desc else ''
    if not dtext or len(dtext) > 1024: errs.append(f'description vacía o > 1024 caracteres ({len(dtext)})')
    comp = re.search(r'^compatibility:\s*(.*)$', fm, re.M)
    if comp and len(comp.group(1)) > 500: errs.append('compatibility > 500 caracteres')
    for p in set(re.findall(r'`((?:config|layers|modules)/[\w./-]+\.md)`', ''.join(f.read_text(encoding='utf-8') for f in d.rglob('*.md') if 'evals' not in f.parts))):
        if not (d / p).exists(): errs.append(f'ruta citada que no existe: {p}')
    return errs, len(dtext)
if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    r = check(target)
    errs, n = r if isinstance(r, tuple) else (r, 0)
    print(f'description: {n} caracteres'); print('\n'.join(errs) or 'OK'); sys.exit(1 if errs else 0)
