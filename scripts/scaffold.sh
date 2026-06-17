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

# Convert kebab-case to camelCase: contains-duplicate -> containsDuplicate
FUNCTION_NAME=$(echo "$PROBLEM_NAME" | sed -E 's/(^|-)([a-z])/\U\2/g' | sed 's/^./\L&/')

mkdir -p "$DIR"

cat > "$DIR/index.ts" << EOF
export function ${FUNCTION_NAME}(): void {}
EOF

cat > "$DIR/index.spec.ts" << EOF
import { describe, it, expect } from 'vitest';
import { ${FUNCTION_NAME} } from '.';

describe('${FUNCTION_NAME}', () => {
  it('should ...', () => {
    expect(${FUNCTION_NAME}()).toBe(undefined);
  });
});
EOF

echo "Created $DIR/"
echo "  - index.ts"
echo "  - index.spec.ts"