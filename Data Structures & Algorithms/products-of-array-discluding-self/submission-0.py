class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        runningF = [0] * len(nums)
        runningB = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                runningF[i]=nums[i]
            else:
                runningF[i]=runningF[i-1]*nums[i]
        
        for i in range ((len(nums)-1), -1, -1):
            if i == (len(nums)-1):
                runningB[i] = nums[i]
            else:
                runningB[i]=runningB[i+1]*nums[i]
    
        output = [0] * len(nums)
        for i, n in enumerate(output):
            if i == 0:
                output[i]=runningB[1]
            elif i == (len(nums)-1):
                output[i]=runningF[i-1]
            else:
                output[i]=runningF[i-1]*runningB[i+1]
        return output