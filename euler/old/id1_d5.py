import math

ub = 1000-1
p = 3
q = 5
pq = p*q

def res():
  n, m, nm = ub//p, ub//q, ub//pq
  sp, sq, spq = p*n*(n+1)/2, q*m*(m+1)/2, pq*nm*(nm+1)/2

  return int(sp + sq - spq)

def brute():
  c = 0

  for i in range(1, ub+1):
    if (i%3 == 0) or (i%5 == 0):
      c+=i

  return c

print(f'math res: {res()}')
# print(f'brute res: {brute()}')
