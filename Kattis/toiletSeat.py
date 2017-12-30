s = input()
up,down,both = 0,0,0

if(s[0] == 'U' and s[1] == 'D'): up += 2; down += 1; both += 1
if(s[0] == 'D' and s[1] == 'U'): down += 2; up += 1; both += 1
if(s[0] == 'D' and s[1] == 'D'): up += 1
if(s[0] == 'U' and s[1] == 'U'): down += 1

for i in range(2,len(s)):
  if(s[i] == 'U'):  down += 2
  elif(s[i] == 'D'):  up += 2
  if(s[i-1] != s[i]): both += 1

print("%d\n%d\n%d" % (up,down,both))