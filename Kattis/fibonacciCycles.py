fib_list = [1, 1]

index = 2

while index < 1000:
    fib_list.append(fib_list[index - 2] + fib_list[index - 1])
    index += 1


def fib(k):

    num_set = []

    for index, fib_num in enumerate(fib_list[2:]):
        val = fib_num % k
        if val not in num_set:
            num_set.append(val)
        else:
            return num_set.index(val) + 2


n = int(input())

for _ in range(n):
    k = int(input())

    print(fib(k))
