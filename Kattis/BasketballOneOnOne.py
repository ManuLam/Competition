s = input()
A,B = s.count('A1') + (s.count('A2')*2), s.count('B1') + (s.count('B2')*2)

print('A' if A > B else 'B')
