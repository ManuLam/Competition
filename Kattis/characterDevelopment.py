import math
n = int(input())
k = [((math.factorial(n) / (math.factorial(int(i)) * math.factorial(n - int(i)))) - 1) for i in range(1,n)]

print(int(sum(k)))