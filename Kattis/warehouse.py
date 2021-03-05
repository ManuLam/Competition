T = int(input())

for _ in range(T):
  K = int(input())
  toys = {}

  for _ in range(K):
    toy_name, toy_amount = input().split()

    if toy_name not in toys:
      toys[toy_name] = int(toy_amount)

    else:
      toys[toy_name] += int(toy_amount)
    
  print(len(toys))

  toys = dict(sorted(toys.items(), key=lambda item: (-item[1], item[0])))

  for key in toys:
    print(key, toys[key])
