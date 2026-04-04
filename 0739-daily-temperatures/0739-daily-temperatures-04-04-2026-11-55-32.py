class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res=[0]*len(t)
        stack=[]
        for i in range(len(t)):
            if not stack:
                stack.append(i)
                continue
            else:
                while stack and t[stack[-1]]<t[i]:
                    res[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return res