export function twoSum(nums: number[], target: number): number[] {
  const differenceMap: Map<number, number> = new Map();

  for (let i = 0; i < nums.length; i++) {
    const difference = target - nums[i];

    const complement = differenceMap.get(nums[i])
    if (complement !== undefined) {
      return [complement, i];
    }
    differenceMap.set(difference, i);
  }

  return [];
}
