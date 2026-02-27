class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool: 
        word1 = sorted(word1)
        word2 = sorted(word2)

        checkone = defaultdict(set)
        checktwo = defaultdict(set)
        
        if word1 == word2:
            return True
        first_count = Counter(word1)
        second_count = Counter(word2)

        for key, val in first_count.items():
            if key not in second_count:
                return False
            checkone[val].add(key)
        for key, val in second_count.items():
            if key not in first_count:
                return False
            checktwo[val].add(key)
        
        
        for i in checkone:
            if i not in checktwo:
                return False
            if len(checkone[i]) != len(checktwo[i]):
                return False
        return True