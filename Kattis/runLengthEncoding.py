operation, s = input().split()
count,curr_letter,output = 1, s[0], ''

if operation == 'E':
  for letter in s[1:]:
    if curr_letter == letter:
      count +=1
    else:
      output += curr_letter + str(count)
      curr_letter = letter
      count = 1
  output += curr_letter + str(count)

else:
  for i in range(0, len(s)-1, 2):
    output += s[i] * int(s[i+1])

print(output)
