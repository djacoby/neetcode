import { describe, it, expect } from 'vitest';
import { isAnagram } from '.';

describe('isAnagram', () => {
  it('should return true when s and t are anagrams', () => {
    expect(isAnagram('racecar', 'carrace')).toBe(true);
  });

  it('should return false when s and t are not anagrams', () => {
    expect(isAnagram('jar', 'jam')).toBe(false);
  });

  it('should return false when s and t are not the same length', () => {
    expect(isAnagram('jar', 'japan')).toBe(false);
  });
});
