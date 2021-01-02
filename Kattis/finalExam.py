n = int(input())
ans_array = [input() for _ in range(n)]


curr_letter = ans_array[0]
points = 0
ans_points = 0

for i in range(1, n):
    if curr_letter == ans_array[i]:
        points += 1
    
    else:
        ans += max(0, points)
        curr_letter = ans_array[i]
        points = 0
    
ans_points += max(0, points)    
print(ans_points)
