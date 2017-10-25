while True:
  val,time = 0,0
  n = int(input()) 
  if n == -1:
    break
  for x in range(n):
    s,t = map(int, input().split())
    val += (s*(t-time))
    time += t-time
  print(val, "miles")
