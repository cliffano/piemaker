#!/usr/bin/env bash
set -o errexit
set -o nounset

# VirtualEnv activation is only needed due to this repo's example structure.
# It's not needed on real PieMaker consumer projects.
cd ../
. ./.venv/bin/activate

printf "\n\n========================================\n"
printf "Show help guide: piemakerexample --help\n"
piemakerexample --help
