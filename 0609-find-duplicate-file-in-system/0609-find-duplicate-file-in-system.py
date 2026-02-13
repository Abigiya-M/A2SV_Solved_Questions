class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for path in paths:
            directory = path.split()
            root = directory[0]
            
            for i in range(1, len(directory)):
                f = -1
                coll = []
                for j in range(len(directory[i])):
                    if directory[i][j] == "(":
                        f = j
                    elif directory[i][j] == ")":
                        k = "".join(coll)
                        store[k].append(root+"/" + directory[i][:f])
                        f = -1
                    else:
                        if f != -1:
                            coll.append(directory[i][j])
                    
        ans = []
        for value in store.values():
            if len(value) > 1:
                ans.append(value)
        
        return ans