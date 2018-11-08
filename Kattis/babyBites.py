def func(l, a):
  for i in range(1, l+1):
    if(a[i-1] not in [str(i), "mumble"]):
      return "something is fishy"
  return "makes sense"

print(func(int(input()), input().split()))