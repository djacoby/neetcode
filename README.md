# NeetCode - Blind 75

Solutions to the [Blind 75](https://neetcode.io/) problems written in TypeScript.

## Setup

```sh
pnpm install
```

## Running Solutions

Solutions are run through vitest. The spec file (`index.spec.ts`) drives the solution (`index.ts`). There are three ways to run them:

**1. CLI**

```sh
pnpm solve src/<group>/<problem>
```

For example:

```sh
pnpm solve src/01-arrays-and-hashing/contains-duplicate
```

**2. Debugger (F5)**

Open a spec file in VS Code and hit F5 (or **Run > Start Debugging**). Breakpoints work in both the spec and solution files.

**3. Vitest extension**

Install the [Vitest extension](https://marketplace.visualstudio.com/items?itemName=vitest.explorer) (already recommended in this workspace) and click the play button next to any test in the spec file to run it directly.

## Structure

Each problem has its own folder containing an implementation and a spec:

```
src/01-arrays-and-hashing/contains-duplicate/
├── index.ts
└── index.spec.ts
```

## Creating a New Problem

```sh
pnpm problem:scaffold <parent-dir> <problem-name>
```

For example:

```sh
pnpm problem:scaffold src/01-arrays-and-hashing contains-duplicate
```

## Problem Groups

| # | Folder | Topic |
|---|--------|-------|
| 01 | `arrays-and-hashing` | Arrays & Hashing |
| 02 | `two-pointers` | Two Pointers |
| 03 | `stack` | Stack |
| 04 | `binary-search` | Binary Search |
| 05 | `sliding-window` | Sliding Window |
| 06 | `linked-list` | Linked List |
| 07 | `trees` | Trees |
| 08 | `tries` | Tries |
| 09 | `heap-priority-queue` | Heap / Priority Queue |
| 10 | `backtracking` | Backtracking |
| 11 | `graphs` | Graphs |
| 12 | `advanced-graphs` | Advanced Graphs |
| 13 | `1-d-dynamic-programming` | 1-D Dynamic Programming |
| 14 | `2-d-dynamic-programming` | 2-D Dynamic Programming |
| 15 | `greedy` | Greedy |
| 16 | `intervals` | Intervals |
| 17 | `math-and-geometry` | Math & Geometry |
| 18 | `bit-manipulation` | Bit Manipulation |
