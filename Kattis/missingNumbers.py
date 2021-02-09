n = int(input())
numbers = [int(input()) for _ in range(n)]

print_range = lambda x,y: [i for i in range(x+1,y)]

ar = []

ar.extend(print_range(0, numbers[0]))

for i in range(len(numbers)-1):
    ar.extend(print_range(numbers[i], numbers[i+1]))

print('\n'.join(map(str, ar)) if len(ar) > 0 else 'good job')
