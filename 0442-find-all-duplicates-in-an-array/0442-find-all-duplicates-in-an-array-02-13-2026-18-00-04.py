class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
       counted = Counter(nums)
       result = []
       for num, count in counted.items():
            if count > 1:
                result.append(num)
       return result 
 