for i in range(int(input())):
  input()
  n = int(input())
  a = [int(input()) for i in range(n)]
  
  print("YES" if (sum(a) % len(a) == 0) else "NO")