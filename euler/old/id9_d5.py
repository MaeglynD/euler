import math

def res():
  # solve a in terms of b, note a^2 + b^2 = (1000-a-b)
  for b in range(1, 500):
    if (a := (2*1e3*b-1e6)/(2*(b-1e3)))%1.0 == 0:
      return int(a*b*(1000-a-b))

def brute():
  return 0

print(f'math res: {res()}')
# print(f'brute res: {brute()}')
