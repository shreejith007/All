import re

def solve(s):
   pat = "^[a-zA-Z0-9-_\.a-z]{1,3$]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return False
   return True

s = "pillai.shreejith32@gmail.com"
print(solve(s))