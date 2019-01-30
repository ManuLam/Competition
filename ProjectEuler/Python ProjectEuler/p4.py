def findPalindrome():
  for i in range(999, 900, -1):
    for j in range(999, 900, -1):
      s = str(i*j)
      if s == s[::-1]:
        return s

print(findPalindrome())