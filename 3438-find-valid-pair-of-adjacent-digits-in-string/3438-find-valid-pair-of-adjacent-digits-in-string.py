class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if cnt[s[i]] == int(s[i]) and cnt[s[i-1]] == int(s[i-1]):
                    return s[i-1: i+1]
        
        return ""