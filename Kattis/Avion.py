FBI = [str(i) for i in range(1, 6) if input().count('FBI') > 0]
print(' '.join(FBI) if FBI else 'HE GOT AWAY!')
