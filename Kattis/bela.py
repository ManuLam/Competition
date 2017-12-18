n,s = input().split()
x,y,k = {'A':'11','K':'4','Q':'3','J':'20','T':'10','9':'14','8':'0','7':'0'}, {'A':'11','K':'4','Q':'3','J':'2','T':'10','9':'0','8':'0','7':'0'}, 0

for i in range(int(n)*4):
  a = input()
  if(a[1] == s):
    k += int(x.get(a[0]))
  else:
    k += int(y.get(a[0]))

print(k)