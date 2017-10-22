import re, collections
p,k,h,t = 13,13,13,13
s = input()
a = re.findall('.{1,3}', s)
c = collections.Counter(a)
for (index, count) in c.most_common():
  if count == 2:
    print("GRESKA")
    break
  else:    
    b = re.findall('(P|K|H|T)', s)
    d = collections.Counter(b)
    print((p-d['P']),(k-d['K']),(h-d['H']),(t-d['T']))
    break