b1,b2,b3,a1,a2 = map(int, input().split())
k,h,c = (b2-b1)*b3,0,0

while(h <= k):
  c += 1
  h += a2
  if(h > k):
    print(a1 + c)