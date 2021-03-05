alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher_text, key = input(), input()
text_length = len(cipher_text)

message = [''] * text_length
new_key = [l for l in key]

for i in range(text_length):
  letter = cipher_text[i]
  shift = alphabet.index(new_key[i])
  shifted_letter = alphabet[alphabet.index(letter) - shift]

  message[i] = shifted_letter
  new_key.append(shifted_letter) 

print(''.join(message))
