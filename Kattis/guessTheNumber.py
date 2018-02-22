def guess(low, high):
  mid = (low + high) / 2
  print(int(mid))
  s = input()
  if(s[0] == 'c'): return ;
  return guess(low,mid-1) if(s[0] == 'l') else guess(mid+1,high)
    
guess(1,1000)