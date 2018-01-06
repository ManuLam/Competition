input()
a = [int(x) for x in input().split() if x[0] != '-']
print(sum(a)/len(a))