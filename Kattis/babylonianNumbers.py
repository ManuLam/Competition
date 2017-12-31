def convert(x,y):
  return x*(60**y)

for i in range(int(input())):
  x,c,k,val = input(), 0, 0, 0
  for j in range(len(x)-1, 0, -1):
    if(x[j] == ','): 
      c += 1
      if(k > 0): 
        val += convert(int(x[j+1:j+k+1]), c-1)
      k = 0
      
    elif(x[j].isdigit()): k += 1
    
  val += convert(int(x[:k+1]), c)
  print(val)