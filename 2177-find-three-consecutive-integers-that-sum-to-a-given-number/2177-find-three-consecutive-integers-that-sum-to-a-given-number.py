class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 :
            return []
        
        base = (num - 3) // 3
        return [base, base + 1, base + 2]
        