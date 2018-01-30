for i in range(int(input())):
  n = input()
  
  if(n[0].isdigit()):
    a = n.split("+")
    print(int(a[0]) + int(a[1]))
  else: 
    print("skipped")