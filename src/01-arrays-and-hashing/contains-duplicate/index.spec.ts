import { describe, it, expect } from 'vitest';
import { hasDuplicate } from '.';

describe('hasDuplicate', () => {
  it('should return true when the array contains duplicates', () => {
    expect(hasDuplicate([1, 2, 3, 3])).toBe(true);
  });

  it('should return false when the array does not contain duplicates', () => {
    expect(hasDuplicate([1, 2, 3, 4])).toBe(false);
  });
});