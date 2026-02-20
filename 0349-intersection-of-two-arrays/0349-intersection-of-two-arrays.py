class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unone = set(nums1)
        untwo = set(nums2)

        ans = []

        for num in unone:
            if num in untwo:
                ans.append(num)
        
        return ans