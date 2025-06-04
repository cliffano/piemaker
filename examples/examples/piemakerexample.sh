#!/usr/bin/env bash
set -o errexit
set -o nounset

cd ../
. ./.venv/bin/activate

printf "\n\n========================================\n"
printf "Show help guide: piemakerexample --help\n"
piemakerexample --help
