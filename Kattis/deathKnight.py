c = 0
for i in range(int(input())):
  s = input()
  if(s.find('CD') == -1):
    c += 1
print(c)