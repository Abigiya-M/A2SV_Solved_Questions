class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSub = max(maxSub, currSum)
        return maxSub
        
nums = [-2,1,-3,4,-1,2,1,-5,4]

x = Solution()
print(x.maxSubArray(nums))
