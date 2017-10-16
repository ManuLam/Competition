x,y,n = map(int, input().split(' '))
for i in range(1,n+1):
  if  i%x == 0 and i%y != 0:
    s = "Fizz"
  elif i%y == 0 and i%x != 0: 
    s = "Buzz"
  elif i%x == 0 and i%y == 0:
    s = "FizzBuzz"
  else:
    s = i
  print(s)
