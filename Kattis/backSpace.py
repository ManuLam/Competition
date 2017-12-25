a = input()
b = [''] *len(a)
c = 0

for i in a:
  if(i != '<'):
    b[c] = i
    c += 1
  elif(i == '<'):
    c -= 1
    b[c] = ''
  
print(''.join(b))