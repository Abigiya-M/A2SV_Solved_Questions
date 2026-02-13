from collections import Counter

class Solution:
    def isSubset(self, a, b):
        countA = Counter(a)
        countB = Counter(b)

        for key in countB:
            if countB[key] > countA[key]:
                return False
        return True
