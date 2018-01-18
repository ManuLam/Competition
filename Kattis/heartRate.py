for i in range(int(input())):
  b,p = map(float, input().split())
  k = 60/b*(b/p)
  print(k*(b-1) , k*b ,k*(b+1))