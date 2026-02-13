t = int(input())

def is_valid(s):
    return ("2026" in s) or ("2025" not in s)

for _ in range(t):
    n = int(input())
    s = input()
    
    
    if is_valid(s):
        print(0)
        continue
    
    chars = ['0', '2', '5', '6']
    answer = 4  

    
    for i in range(n):
        for c in chars:
            new_s = s[:i] + c + s[i+1:]
            if is_valid(new_s):
                answer = 1
                break
        if answer == 1:
            break
    
    print(answer)
