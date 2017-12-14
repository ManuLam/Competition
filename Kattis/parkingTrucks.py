a,b,c = map(int, input().split())
t1s,t1f = map(int, input().split())
t2s,t2f = map(int, input().split())
t3s,t3f = map(int, input().split())
t1 = [int(x) for x in range(t1s, t1f)]
t2 = [int(x) for x in range(t2s, t2f)]
t3 = [int(x) for x in range(t3s, t3f)]
total = 0

for i in range (1,101):
  if(i in t1 and i in t2 and i in t3):
    total += c*3
    
  elif(i in t1 and i in t2):
    total += b*2
    
  elif(i in t2 and i in t3):
    total += b*2
    
  elif(i in t1 and i in t3):
    total += b*2
    
  elif((i in t1) or (i in t2) or (i in t3)):
    total += a

print(total)