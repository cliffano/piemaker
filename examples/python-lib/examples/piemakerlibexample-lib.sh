#!/usr/bin/env bash
set -o errexit
set -o nounset

cd ../
. ./.venv/bin/activate
cd examples/

python3 _piemakerlibexample.py