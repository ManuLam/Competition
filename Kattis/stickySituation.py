_,a  = input(), sorted(list(map(int, input().split())))
b = [1 for i in range(len(a)-1,0,-2) if(((a[i-2]+a[i-1]) > a[i]) and (a[i]+a[i-1] > a[i-2]) and (a[i]+a[i-2] > a[i-1]))]

print("possible" if(len(b) > 0) else "impossible")