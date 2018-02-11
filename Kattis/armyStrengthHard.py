for i in range(int(input())):
  space = input()
  g,m = input().split()
    
  gA = list(map(int, input().split()))
  mA = list(map(int, input().split()))
    
  print("Godzilla" if max(gA) >= max(mA) else "MechaGodzilla")