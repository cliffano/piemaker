#!/usr/bin/bash
set -o nounset

cd ../
. ./.venv/bin/activate
cd examples/

printf "\n\n========================================\n"
printf "Show help guide:\n"
piemakerexample --help

printf "\n\n========================================\n"
printf "Show version info: piemakerexample --version\n"
piemakerexample --version

printf "\n\n========================================\n"
printf "Run command with default config file:\n"
piemakerexample

printf "\n\n========================================\n"
printf "Run command with specified config file:\n"
piemakerexample --conf-file piemakerexample.yaml

printf "\n\n========================================\n"
printf "Run command with specified config file and custom flags:\n"
piemakerexample --conf-file piemakerexample.yaml --reverse --transformation upper
