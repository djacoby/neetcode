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
IFS='-' read -ra PARTS <<< "$PROBLEM_NAME"
FUNCTION_NAME="${PARTS[0]}"
for part in "${PARTS[@]:1}"; do
  first=$(echo "${part:0:1}" | tr 'a-z' 'A-Z')
  FUNCTION_NAME+="${first}${part:1}"
done

# Convert kebab-case to Title Case: contains-duplicate -> Contains Duplicate
TITLE_NAME=""
for part in "${PARTS[@]}"; do
  first=$(echo "${part:0:1}" | tr 'a-z' 'A-Z')
  TITLE_NAME+="${first}${part:1} "
done
TITLE_NAME="${TITLE_NAME% }"

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

cat > "$DIR/README.md" << EOF
# ${TITLE_NAME}

**Difficulty:**

## Problem

## Examples

### Example 1:

**Input:**

**Output:**

## Constraints

## Solution

## Time & Space Complexity
EOF

echo "Created $DIR/"
echo "  - index.ts"
echo "  - index.spec.ts"
echo "  - README.md"