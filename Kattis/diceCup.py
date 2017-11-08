from collections import Counter
x,y = map(int,input().split())
a = []
for i in range(1,x+1):
	for j in range(1,y+1):
		a.append(i+j)
		
c  = list(Counter(a).most_common()[0])
for value, count in Counter(a).most_common():
  if(count == c[1]):
    print(value)
  else:
    break