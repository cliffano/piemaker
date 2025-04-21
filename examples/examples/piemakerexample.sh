#!/usr/bin/env bash
set -o errexit
set -o nounset

cd ../ && . ./.venv/bin/activate && piemakerexample --help
