class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minVal = nums[0]
        while l <= r:
            mid = (l + r)//2
            minVal = min(minVal, nums[mid])
            #we're in the left sorted portion
            if nums[mid] >= nums[0]:
                l = mid + 1
            #right sorted portion
            else:
                r = mid - 1
        return minVal
