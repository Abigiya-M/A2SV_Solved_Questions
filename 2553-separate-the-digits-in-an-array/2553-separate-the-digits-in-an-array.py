class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            coll = []
            while num:
                rem = num % 10
                num = num // 10
                coll.append(rem)
            coll.reverse()
            answer.extend(coll)
        
        return answer