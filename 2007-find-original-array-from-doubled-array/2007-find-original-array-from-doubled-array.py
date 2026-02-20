class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        changed.sort()
        coll = []

        for i in changed:
            double = i * 2

            if double in cnt and i in cnt:
                cnt[double] -= 1

                if cnt[double] == 0:
                    del cnt[double]
                
                cnt[i] -= 1
                if cnt[i] == 0:
                    del cnt[i]

                coll.append(i)
        
        print(cnt)
        if len(cnt) == 0:
            return coll 
        
        return []


            
