n,expenses = input(), list(map(int, input().split()))

print(-sum([val for val in expenses if val < 0]))
