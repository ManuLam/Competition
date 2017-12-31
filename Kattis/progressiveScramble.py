alphabet = ' abcdefghijklmnopqrstuvwxyz'
def encrypt(s):
  e,k = '',0
  for i in range(len(s)):
    e += alphabet[(k + alphabet.index(s[i])) % 27]
    k += alphabet.index(s[i])
  return e

def decrypt(s):
  d,k = '',0
  for i in range(len(s)-1, 0, -1):
    d += alphabet[alphabet.index(s[i]) - alphabet.index(s[i-1])]
  d += s[0]
  return d[::-1]

for i in range(int(input())):
  s = input()
  if(s[0] == 'e'):
    print(encrypt(s[2:]))
  else:
    print(decrypt(s[2:]))