from datetime import datetime
while True:
  try:
    s = input().split()
    d1 = datetime.strptime(s[len(s)-2], "%H:%M")
    d2 = datetime.strptime(s[len(s)-1], "%H:%M")
    d = str(d2-d1)[:-3]
    h,m = d.split(':')

    print(' '.join(s[:len(s)-2]) ,"%d hours %d minutes" % (int(h), int(m)))

  except EOFError:
    break