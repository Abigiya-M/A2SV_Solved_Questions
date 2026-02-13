t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    found = False
    
    for i in range(1, n):
        a = s[:i]
        b = s[i:]
        
        
        if a[0] == '0' or b[0] == '0':
            continue
        
      
        a_num = int(a)
        b_num = int(b)
        
        if b_num > a_num:
            print(a_num, b_num)
            found = True
            break
    
    if not found:
        print(-1)
