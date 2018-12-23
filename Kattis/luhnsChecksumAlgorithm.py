for _ in range(int(input())):
  count,total = 0,0
  s = input()

  for i in range(len(s)-1,-1,-1):
    k = int(s[i])
    if(count%2 != 0): total += ((k*2)-9) if k > 4 else (k*2)
    else: total += k

    count += 1

  if(total%10 == 0):  print('PASS')
  else: print('FAIL')