class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        cnt = defaultdict(int)
        for response in responses:
            unique = set(response)

            for val in unique:
                cnt[val] += 1
        
        pot = []
        for key, value in cnt.items():
            pot.append([value, key])
        
        pot.sort()
        targ = pot[-1][0]
        
        for key, value in pot:
            if key == targ:
                return value





        