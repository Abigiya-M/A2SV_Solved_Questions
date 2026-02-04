t = int(input())
for _ in range(t):
    n = int(input())   
    a = input().strip()

    s = ""
    for ch in a:
        s = min(ch + s, s + ch)

    print(s)
