s = input()
print(1 if (lambda x,y: x == 2*y)(len(s), s.count('B')) else 0)