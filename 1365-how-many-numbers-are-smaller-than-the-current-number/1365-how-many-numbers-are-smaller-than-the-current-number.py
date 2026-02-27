class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums = [[nums[i], i] for i in range(len(nums))]

        ans = [-1 for i in range(len(nums))]

        nums.sort()

        for i in range(len(nums)):
            val, ind = nums[i]

            curr = i
            while curr > -1 and nums[curr][0] == val:
                curr -= 1
            
            ans[ind] = curr + 1

        return ans


