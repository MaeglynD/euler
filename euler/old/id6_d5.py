import math

# Anon, you did find the closed form of sum k^2 before opening your IDE, right...?
def res(n):
  a = ((n*(n+1))/2)**2
  b = (1/3)*((n**3) + (3/2)*(n**2) + (1/2)*n)
  
  return int(a - b)

def brute(n):
  return sum(range(n+1))**2 - sum([x**2 for x in range(n+1)])

print(f'math res: {res(100)}')
# print(f'brute res: {brute(100)}')
