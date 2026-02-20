class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnta = Counter(ransomNote)
        cntb = Counter(magazine)
        flag = True

        for k in cnta.keys():
            if k not in cntb:
                flag = False
            
            elif cntb[k] < cnta[k]:
                flag = False
            
            if not flag:
                break
        
        if not flag:
            return False
        
        return True
    
