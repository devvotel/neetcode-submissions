class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                j = hashmap[target - nums[i]]
                if (i != j):
                    return [i,j]
        