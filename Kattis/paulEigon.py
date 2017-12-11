a,b,c = map(int, input().split())
print("paul" if(int((b+c) / a) % 2 == 0 or (b+c) <= a) else "opponent")