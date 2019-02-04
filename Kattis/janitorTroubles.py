x = list(map(int, input().split()))
s = (x[0]+x[1]+x[2]+x[3])/2

print('{0:.7g}'.format(((s-x[0])*(s-x[1])*(s-x[2])*(s-x[3]))**.5))