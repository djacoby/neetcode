export function hasDuplicate(nums: number[]): boolean {
  return new Set(nums).size < nums.length;
}