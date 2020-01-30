n,line = int(input()), list(map(int, input().split()))
line_order = [(i+2, line[i]) for i in range(n-1)]

print(1, ' '.join(map(str, [x for x,y in sorted(line_order, key=lambda x: x[1])])))
