a,b = 1,1
temp = total = 0

while b < 4000000:
	a,b = b, a+b
	total += b if b%2 == 0 else 0

print total
