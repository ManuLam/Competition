s1, s2 = input(), input()

s1_count, s2_count = s1.count('S'), s2.count('S')
product = s1_count * s2_count

print( 'S(' * product + '0' + ')' * product  if product != 0 else 0)
