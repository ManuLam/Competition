n = int(input())
vals = [list(map(float, input().split())) for i in range(n)]

print(sum([((vals[i][1] + vals[i+1][1])/2) * (vals[i+1][0] - vals[i][0]) for i in range(len(vals)-1)])/1000)
