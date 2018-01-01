k = {'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,'t':8,'u':8,'v':8,'w':9,'x':9,'y':9,'z':9}
a,t = ["0","","abc", "def" ,"ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], 0

for i in range(int(input())):
  s,s1,cache = [x for x in input()],'', -1

  for j in s:
    if(j.isspace()):
      if(cache == 0): s1 += ' 0';
      else: s1 += '0'
      cache = 0
    else:
      val = str(k.get(j)) * (a[k.get(j)].index(j)+1)
      
      if(k.get(j) == cache):  s1 += " " + val
      else: s1 += val
  
      cache = k.get(j)
      
  print("Case #%d: %s" % (i+1,s1))