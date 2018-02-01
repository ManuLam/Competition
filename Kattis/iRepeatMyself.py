def check(s):
  for i in range(1, len(s)+1):
  	if(i == len(s) or s[i] == s[0]):
	    if(s == (s[:i]*int((len(s)/i)+1))[:len(s)]):
	      return len(s[:i])

for i in range(int(input())):
  a = input()
  print(check(a))