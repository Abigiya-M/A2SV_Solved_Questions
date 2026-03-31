class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = len(nums) // 3

        count = Counter(nums)

        ans = []

        for num in count:
            if count[num] > cnt:
                ans.append(num)
        
        return ans