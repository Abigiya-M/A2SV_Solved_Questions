class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x: len(x))

        ans = ""

        for i in range(len(strs[0])):
            flag = True
            for j in range(len(strs)):
                if i < len(strs[j]) and strs[0][i] != strs[j][i]:
                    flag = False
                    break
            
            if not flag:
                break
            else:
                ans = strs[0][:i + 1]


        return ans