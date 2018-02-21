k = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..","J": ".---","K": "-.-","L": ".-..",
"M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--", "X": "-..-", "Y": "-.--",
"Z": "--..", "_": "..--", ".": "---.", ",": ".-.-", "?": "----"}

kr,fin = {y:x for x, y in k.items()}, []
while True:
  try:
    s = input()
    a,b,c,p = ''.join([k[i] for i in s]), [len(k[i]) for i in s][::-1], 0, []
    
    for i in b:
      p.append(kr[a[c:c+i]])
      c += i
      
    fin.append(''.join(p))
      
  except EOFError:
    print('\n'.join(fin))
    break