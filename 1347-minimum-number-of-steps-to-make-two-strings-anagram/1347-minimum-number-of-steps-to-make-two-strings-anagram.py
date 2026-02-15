class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(t)

        fir, sec = 0, 0
        for cnt in cnt_s:
            if cnt_s[cnt] > cnt_t[cnt]:
                fir += cnt_s[cnt] - cnt_t[cnt]
        
        for cnt in cnt_t:
            if cnt_t[cnt] > cnt_s[cnt]:
                sec += cnt_t[cnt] - cnt_s[cnt]
        
        return min(fir, sec)
