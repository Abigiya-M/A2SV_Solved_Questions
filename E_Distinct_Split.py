t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = 0

    for i in range(1, n):   
        left = s[:i]
        right = s[i:]

        left_distinct = len(set(left))
        right_distinct = len(set(right))

        ans = max(ans, left_distinct + right_distinct)

    print(ans)

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input()

#     right = {}   
#     for ch in s:
#         right[ch] = right.get(ch, 0) + 1

#     left = {}
#     left_distinct = 0
#     right_distinct = len(right)

#     ans = 0

#     for i in range(n - 1): 
#         ch = s[i]

#         # move ch to left
#         if ch not in left:
#             left_distinct += 1
#             left[ch] = 1
#         else:
#             left[ch] += 1

#         # remove ch from right
#         right[ch] -= 1
#         if right[ch] == 0:
#             right_distinct -= 1

#         ans = max(ans, left_distinct + right_distinct)

#     print(ans)
