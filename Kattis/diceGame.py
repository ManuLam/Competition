a,b = list(map(int, input().split())), list(map(int, input().split()))

if(sum(a) > sum(b)):
  print("Gunnar")
elif(sum(b) > sum(a)):
  print("Emma") 
else:
   print("Tie")