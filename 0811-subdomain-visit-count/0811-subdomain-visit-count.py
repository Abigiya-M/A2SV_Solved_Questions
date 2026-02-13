class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = defaultdict(int)

        for domain in cpdomains:
            val, dom = domain.split()

            dom = dom.split(".")
            
            curr = ""
            for i in range(len(dom)-1, -1, -1):
                if len(curr) > 1:
                    curr = dom[i] + "." + curr
                else:
                    curr = dom[i]
                
                store[curr] += int(val)

        
        
        ans = []
        for key, val in store.items():
            ans.append(f"{val} {key}")

        return ans
