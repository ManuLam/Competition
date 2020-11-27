_,vals = input(), list(map(int, input().split()))

pair_vals = [(vals[i], vals[i+2]) for i in range(len(vals)-2)]
i,m = -1, 41

for val in pair_vals:
  if max(val[0], val[1]) < m:
    m = max(val[0], val[1])
    i = pair_vals.index(val)

print(i+1, m)
