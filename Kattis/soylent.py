for i in range(int(input())):
  x = int(input())
  print(int(x/400)) if x % 400 == 0 else print(int(x/400)+1)