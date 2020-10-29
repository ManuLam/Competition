for _ in range(int(input())):
  K,N = map(int, input().split())
  
  print(K, int((N*(N+1)/2) + N))
