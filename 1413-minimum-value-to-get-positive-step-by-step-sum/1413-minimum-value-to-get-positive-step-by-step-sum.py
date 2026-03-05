class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = 0
        sm = 0

        for i in range(len(nums)):
            sm += nums[i]
            if sm < 0:
                curr = min(sm, curr)
        
        return abs(curr) + 1
        