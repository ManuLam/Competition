c = 0
while True:
  n = int(input())
  if(n == 0): break

  amtimes,pmtimes = [], []
  c += 1; 
  if(c > 1): print()

  for i in range(n):
    s = input()
    if(s.split()[1] == "a.m."): amtimes.append(s)
    else: pmtimes.append(s)
    
  amtimes.sort(key = lambda x: (int(x.split()[0].split(':')[0]) % 12, int(x.split()[0].split(':')[1])))
  pmtimes.sort(key = lambda x: (int(x.split()[0].split(':')[0]) % 12, int(x.split()[0].split(':')[1])))

  print('\n'.join(amtimes) + "\n" + '\n'.join(pmtimes))