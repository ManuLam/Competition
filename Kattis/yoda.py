a,b,s1,s2 = input(), input(), "",""

while(len(a) > len(b)):
  b = '0' + b
while(len(b) > len(a)):
  a = '0' + a

for i in range(len(a)):
  if(int(a[i]) >= int(b[i])):
    s1 += a[i]
    
  if(int(a[i]) <= int(b[i])):
    s2 += b[i]

print(str(int(s1)) if len(s1) > 0 else "YODA")
print(str(int(s2)) if len(s2) > 0 else "YODA")