for i in range(int(input())):
  s = list(map(int, input().split()))
  for y in range(1,len(s)-1):
    if((s[y] + 1) != s[y+1]):
      print((y+1))
      break;