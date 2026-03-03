class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = [0 for i in range(26)]
        start = 0
        answer = 0
        for i in range(len(s)):
            c[ord(s[i]) - ord('A')] += 1
            
            while (sum(c) - max(c)) > k:
                c[ord(s[start]) - ord('A')] -= 1
                start += 1
            
            answer = max(answer, i - start + 1)
        return answer