N = int(input())

ar = [input().lower() for x in range(N)] 
result = [min(s.count('pink') + s.count('rose'), 1) for s in ar]

print(sum(result) if sum(result) > 0 else 'I must watch Star Wars with my daughter')
