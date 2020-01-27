a,b = map(int, input().split())
k = {i:{'A':0, 'B':0}  for i in range(1, b+1)}
A_total_wasted, B_total_wasted,total_votes = 0,0,0

for _ in range(a):
  district,A,B = map(int, input().split())
  k[district]['A'] += A
  k[district]['B'] += B

for district,vals in k.items():
  A,B = vals['A'],vals['B']
  min_votes = abs(A+B)/2 + 1
  A_wasted,B_wasted,total_votes = A,B,total_votes+A+B

  if A > B:
    A_wasted = int(-(- max(0, A - min_votes) // 1))
  else:
    B_wasted = int(-(- max(0, B - min_votes) // 1))

  A_total_wasted += A_wasted
  B_total_wasted += B_wasted

  print('A' if A > B else 'B', A_wasted, B_wasted)

print(abs(A_total_wasted-B_total_wasted)/total_votes)
