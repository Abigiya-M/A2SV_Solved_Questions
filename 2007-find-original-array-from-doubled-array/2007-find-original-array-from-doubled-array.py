class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        changed.sort()
        coll = []

        for i in changed:
            double = i * 2

            if double in cnt and i in cnt and len(cnt) > 1:
                del cnt[double]
                del cnt[i]
                coll.append(i)
        
        if len(cnt) == 0:
            return coll 
        
        return []


            
