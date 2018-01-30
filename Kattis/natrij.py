from datetime import datetime
x,y = input(), input()
s = (" " + str(datetime.strptime(y, '%H:%M:%S') - datetime.strptime(x, '%H:%M:%S')))[-8:]

if(x == y): print("24:00:00")
else: print(s if(s[0] != " ") else "0" + s[1:])