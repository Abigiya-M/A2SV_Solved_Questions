class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 1:
             multiple = 2*n
        else:
            multiple = n
        return multiple