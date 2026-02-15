class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()

        while n:
            sm = 0

            while n:
                sm += (n % 10) ** 2
                n = n // 10
            
            if sm == 1:
                return True
            
            if sm in check:
                return False
            
            check.add(sm)

            n = sm
        
        return True
