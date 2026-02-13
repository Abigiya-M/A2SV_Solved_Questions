class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)

        ans = []
        for i in range(1, len(nums)+1):
            if cnt[i] == 2:
                ans.append(i)

        return ans
