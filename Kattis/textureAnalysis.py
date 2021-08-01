index = 1

while 1:
    s = input()

    if s == 'END':
        break

    uncommons = set(s[1:-1].split('*'))

    print('{} {}'.format(index, 'EVEN') if len(uncommons) <= 1 and s[0] == s[-1] else '{} {}'.format(index, 'NOT EVEN'))
    index += 1
