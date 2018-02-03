a,b = int(input()), int(input())

if(a > b and abs(a-b) >= 180):  print(360 - abs(a-b))
elif(a > b and abs(a-b) < 180): print(-abs(a-b))
elif(b > a and abs(a-b) > 180):  print(-360 + abs(a-b))
elif(b > a and abs(a-b) <= 180): print(abs(a-b))
else: print(0)