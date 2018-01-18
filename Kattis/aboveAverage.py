for i in range(int(input())):
 a = list(map(int, input().split()))
 k = sum(a[1:])/a[0]
 h = sum([1 for x in a[1:] if x > k])
 
 print("%.3f%s" % (h/a[0]*100,"%"))