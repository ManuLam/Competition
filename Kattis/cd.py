import sys


def get_str():
    return sys.stdin.readline().strip()

def get_int():
    return int(sys.stdin.readline().strip())

def get_ints():
    return map(int, sys.stdin.readline().strip().split())

def check(aAr, bAr):
    i, j, cn = 0, 0, 0

    while i < len(aAr) and j < len(bAr):
        if aAr[i] < bAr[j]:
            i += 1
        elif aAr[i] > bAr[j]:
            j += 1
        else:
            i += 1
            j += 1
            cn += 1
    return cn


k = []
while True:
    n,m = map(int, input().split())

    if n == 0 and m == 0:
        break

    a = [get_int() for _ in range(n)]
    b = [get_int() for _ in range(m)]

    k.append(check(a, b))

print('\n'.join(map(str, k)))
