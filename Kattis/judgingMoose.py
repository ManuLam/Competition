a,b = map(int, input().split())
if a != b:
	s = ("Odd %d" % (max(a,b)*2))
elif a == b and (a != 0 and b != 0):
	s = ("Even %d" % (a*2))
else: 
  s = "Not a moose"
  
print(s)