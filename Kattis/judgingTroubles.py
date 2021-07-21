import sys

def get_str():
    return sys.stdin.readline().strip()


n = int(input())

count_map_dom = {}
count_map_kattis = {}

dom = [get_str() for _ in range(n)]
kattis = [get_str() for _ in range(n)]

for word in dom:
    if word not in count_map_dom:
        count_map_dom[word] = 1
    else:
        count_map_dom[word] += 1

for word in kattis:
    if word not in count_map_kattis:
        count_map_kattis[word] = 1
    else:
        count_map_kattis[word] += 1

total = 0

for k,v in count_map_kattis.items():
    if k in count_map_dom:
        total += min(v, count_map_dom[k])

print(total)
