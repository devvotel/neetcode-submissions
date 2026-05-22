class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            seen[num] = i
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen and seen[needed]!=i:
                return [i, seen[needed]]