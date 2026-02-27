class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        mp_1 = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for i, val in enumerate(pattern):
            if val in mp or s[i] in mp_1:
                if val in mp:
                    if s[i] != mp[val]:
                        return False
                else:
                    if mp_1[s[i]] != val:
                        return False
            else:
                mp[val] = s[i]
                mp_1[s[i]] = val
        return True