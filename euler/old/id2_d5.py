import math

ub = 4000000

# where i come from, you dont ask about accuracy over n=50. 
def fib(n):
  phi = (1 + math.sqrt(5))/2
  psi = -1/phi
  coef = 1/(phi-psi)

  return int(coef*(phi**n) -coef*(psi**n))

def res():
  total, i = 0, 3

  while (n := fib(i)) < ub:
    total+=n
    i+=3
  
  return total

def brute():
  total = 0
  a = 0
  b = 1

  while (c := a+b) < ub: 
    a = b
    b = c

    if (c%2 == 0):
      total+=c
  
  return total

print(f'math res: {res()}')
# print(f'brute res: {brute()}')
