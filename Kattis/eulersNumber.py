total,prev = 1,1
for i in range(1, int(input())+1):
  total += prev*(1/i)
  prev *= 1/i
print(total)