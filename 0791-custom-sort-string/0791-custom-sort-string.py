class Solution:
    def customSortString(self, order: str, s: str) -> str:
        alphabet = defaultdict(int)

        for i in range(len(order)):
            alphabet[order[i]] = i
        
        answer = defaultdict(list)

        for i, val in enumerate(s):
            if val in alphabet:
                answer[alphabet[val]].append(val)
            else:
                answer[i].append(val)
        ans = []
        for i in range(len(s)):
            ans.extend(answer[i])

        return "".join(ans)