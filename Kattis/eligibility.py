for i in range(int(input())):
  s = input().split()
  name,study,born,courses = s[0],s[1][:4], s[2][:4], s[-1] 
  
  if(int(study) >= 2010 or int(born) >= 1991):
    print("%s eligible" % (name))
    
  elif(int(courses) > 40):
    print("%s ineligible" % (name))
    
  else:
    print("%s coach petitions" % (name))