n, k = map(int, input().split())
scores = list(map(int, input().split()))

passed_students = 0
kth_score = scores[k - 1]

for score in scores:
    if score >= kth_score and score > 0:
        passed_students += 1

print(passed_students)
