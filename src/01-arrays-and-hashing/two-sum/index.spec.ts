import { describe, it, expect } from 'vitest';
import { twoSum } from '.';

describe('twoSum', () => {
  it('should return [0, 1] for nums = [3, 4, 5, 6] & target = 7', () => {
    expect(twoSum([3, 4, 5, 6], 7)).toStrictEqual([0, 1]);
  });

  it('should return [0, 2] for nums = [4, 5, 6] & target = 10', () => {
    expect(twoSum([4, 5, 6], 10)).toStrictEqual([0, 2]);
  });

  it('should return [0, 1] for nums = [5, 5] & target = 10', () => {
    expect(twoSum([5, 5], 10)).toStrictEqual([0, 1]);
  });
});

