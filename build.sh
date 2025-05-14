#!/bin/zsh

REPO_NAME="markdown-renderer"

python3 src/main.py "/${REPO_NAME}/"

echo "Site built successfully in docs/ directory"
echo "Base path set to: /${REPO_NAME}/"

