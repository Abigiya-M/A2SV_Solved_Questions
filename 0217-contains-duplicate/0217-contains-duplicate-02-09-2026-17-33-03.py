class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counted = Counter(nums)
        for count in counted.values():
            if count > 1:
                return True
        return False