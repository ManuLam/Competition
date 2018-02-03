def within(r, c):
  if((r >= 5 or r < 0) or (c >= 5 or c < 0)): return False
  return True

def check(r, c, ar):
  if((within(r+2,c+1) and ar[r+2][c+1] == "k") or (within(r+2,c-1) and ar[r+2][c-1] == "k")): return False
  if((within(r-2,c+1) and ar[r-2][c+1] == "k") or (within(r-2,c-1) and ar[r-2][c-1] == "k")): return False
  
  if((within(r+1,c+2) and ar[r+1][c+2] == "k") or (within(r+1,c-2) and ar[r+1][c-2] == "k")): return False
  if((within(r-1,c-2) and ar[r-1][c-2] == "k") or (within(r-1,c+2) and ar[r-1][c+2] == "k")): return False

  return True
  

def isvalid(ar):
  c = 0
  for i in range(5):
    for j in range(5):
      if(ar[i][j] == "k"):
        c += 1
        if(not check(i,j,ar)): return False
  
  return True if c == 9 else False

a = [input() for x in range(5)]
print("valid" if isvalid(a) else "invalid")