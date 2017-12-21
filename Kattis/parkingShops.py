for i in range(int(input())):
  n = input()
  a = sorted(list(map(int, input().split())))
  print((a[len(a)-1] - a[0])*2)