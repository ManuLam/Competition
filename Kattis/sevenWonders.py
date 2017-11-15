import collections
l = list(input())
l.sort()
val = 0
counter = collections.Counter(l)
t = counter['T']
c = counter['C']
g = counter['G']
if t == c == g:
  val += t*7
elif t > 0 and c > 0 and g > 0:
  least_common = collections.Counter(l).most_common()[-1]
  val += least_common[1]*7
for letter in 'TCG':
  val += int(counter[letter])**2
print(val)