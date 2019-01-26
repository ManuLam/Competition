q = 0
for x in range(1000):
	q += x if x%3 == 0 or x%5 == 0 else 0
print q