for _ in range(int(input())):
  outlets = list(map(int, input().split()))[1:]

  print(sum(outlets) - len(outlets) + 1)
