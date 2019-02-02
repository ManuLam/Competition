def findPythagoreanTriplet():
  for a in range(1,500):
    for b in range(a+1,500):
      if (a**2+b**2)**.5 == int((a**2+b**2)**.5): 
        if a + b + (a**2+b**2)**.5 == 1000: 
          return(a*b*int((a**2+b**2)**.5))

print(findPythagoreanTriplet())