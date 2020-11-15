C,K = input(), input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
output = ''

for i in range(len(C)):
  i1,i2 = alphabet.find(C[i]), alphabet.find(K[i])  
  output += alphabet[(i1 + i2) % 26] if i % 2 == 1 else alphabet[(i1 - i2) % 26]

print(output)
