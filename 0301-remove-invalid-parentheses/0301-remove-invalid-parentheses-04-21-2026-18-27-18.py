from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        dq = deque([s])
        seen, res = set(), []
        while dq:
            cnt_s = len(dq)
            for i in range(cnt_s):
                string = dq.popleft()
                if isvalid(string):
                    res.append(string)
                if not res:
                    # at current level, we haven't found any valid string yet
                    for j in range(len(string)):
                        if string[j] == '(' or string[j] == ')':
                            next_str = string[:j] + string[j+1:]
                            if next_str not in seen:
                                seen.add(next_str)
                                dq.append(next_str)
        return res
                
        
def isvalid(s):
    dic = {'(': 1, ')': -1}
    count = 0
    for char in s:
        count += dic.get(char, 0)
        if count < 0:
            return False # early exit coz once count of ')' > '(', s can't be valid
    return count == 0