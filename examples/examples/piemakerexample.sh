#!/usr/bin/env bash
set -o errexit
set -o nounset

cd ../
. ./.venv/bin/activate

echo "\n\n========================================"
echo "Show help guide: piemakerexample --help"
piemakerexample --help
