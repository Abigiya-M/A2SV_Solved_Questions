class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        ans = 0

        for num in check:

            if num - 1 not in check:
                cnt = 1
                while num + cnt in check:
                    cnt += 1
            
                ans = max(ans, cnt)

        return ans            

        