#!/bin/sh
# CLI wrapper para ejecutar el pipeline de ARES-11 (versión enterprise)
python interfaces/cli/ares11.py --stage full "$@"
