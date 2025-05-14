#!/bin/zsh
python ./src/main.py
cd docs && python -m http.server 8888
