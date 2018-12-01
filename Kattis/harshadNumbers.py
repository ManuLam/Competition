val = int(input())

while(1):
  if(val % sum([int(x) for x in str(val)]) == 0): 
    print(val)
    break
  else:
    val += 1