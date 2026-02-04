t = int(input())
for _ in range(t):
    word = input()
    if len(word) > 10:
        mid= len(word)-2 
        print(f"{word[0]}{mid}{word[-1]}")
    else:
        print (f"{word}")
