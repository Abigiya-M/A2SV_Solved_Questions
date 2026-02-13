class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counted = Counter(nums)
        for num, count in counted.items():
            if count == 1:
                return num