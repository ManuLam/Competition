def calc(s, t, time):
  if(s == 'F'): return(time + t if(time + t < 1440) else time + t - 1440)
  if(s == 'B'): return(time - t if(time - t >= 0) else time - t + 1440)

for _ in range(int(input())):
  a = input().split()
  k = calc(a[0], int(a[1]), (int(a[2])*60) + int(a[3]))
  print(int(k/60), (k%60))