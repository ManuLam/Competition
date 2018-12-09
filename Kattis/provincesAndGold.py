G,S,C = map(int, input().split())

G *= 3; S *= 2; C *= 1
total,t = G+S+C, False

k = {8:'Province', 5:'Duchy', 2:'Estate'}
h = {6:'Gold', 3:'Silver', 0:'Copper'}

for x in k:
  if total >= x:
    print(k[x],end="")
    t = True
    break

for x in h:
  if(total >= x):
    print(" %s %s" % ("or", h[x]) if t == True else h[x])
    break