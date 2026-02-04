class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = str(x)
        l = len(p)
        for i in range(l//2):
            if p[i] != p[l-i-1]:

                return False 

        return True