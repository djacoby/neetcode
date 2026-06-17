#!/bin/bash
set -e

if [ $# -lt 2 ]; then
  echo "Usage: pnpm problem:scaffold <parent-dir> <problem-name>"
  echo "Example: pnpm problem:scaffold src/01-arrays-and-hashing contains-duplicate"
  exit 1
fi

PARENT_DIR="$1"
PROBLEM_NAME="$2"
DIR="$PARENT_DIR/$PROBLEM_NAME"

mkdir -p "$DIR"
touch "$DIR/index.ts"
touch "$DIR/index.spec.ts"

echo "Created $DIR/"
echo "  - index.ts"
echo "  - index.spec.ts"