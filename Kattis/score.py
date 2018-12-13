def toSec(s):
  t = s.split(':')
  return (int(t[0])*60)+int(t[1])

def toMin(s):
  return "%d:%02d" % (s//60, s%60)

H,htime,A,atime = 0,0,0,0

size = int(input())
s = [input().split() for i in range(size)]

for i in range(len(s)-1):
  t1,t2 = s[i+1][2], s[i][2]

  timeStored = toSec(t1) - toSec(t2)

  if(s[i][0] == 'H'): H += int(s[i][1])
  else: A += int(s[i][1])

  if(H > A):
    htime += timeStored
  elif(A > H):
    atime += timeStored

if(s[-1][0] == 'H'): H += int(s[-1][1])
else: A += int(s[-1][1])

if(H > A):
  htime += (32*60) - toSec(s[-1][2])
  print('H', toMin(htime), toMin(atime))

elif(A > H):
  atime += (32*60) - toSec(s[-1][2])
  print('A', toMin(htime), toMin(atime))