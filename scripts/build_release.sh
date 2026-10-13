#!/usr/bin/env bash
# Builds dist/business-launcher.zip for claude.ai: one root folder named exactly like the skill,
# with only the files the skill needs at runtime. Validates the skill first.
set -euo pipefail
cd "$(dirname "$0")/.."
python scripts/validate_skill.py .
mkdir -p dist
rm -f dist/business-launcher.zip
git archive --format=zip --prefix=business-launcher/ -o dist/business-launcher.zip HEAD SKILL.md LICENSE config layers modules
unzip -l dist/business-launcher.zip
