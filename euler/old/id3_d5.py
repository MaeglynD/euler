import math

# if you want performance, solve the riemman hypothesis.
# until then i'm not giving you you're unknown distribution 
# in anything but O(spaghetti).
def prime_gen(n):
  nums = list(range(0, n+1))
  primes = [2]
  curr = 2

  while True:
    old_curr = curr

    for i in range(curr, n+1, curr):
      nums[i] = False

    for i in range(curr+1, n+1):
      if nums[i]:
        primes.append(i)
        curr = i
        break
    
    if old_curr == curr:
      break
  
  return primes

def res(n):
  primes = prime_gen(10000)
  curr = 1

  for p in primes:
    while n % p == 0:
      curr = max(curr, p)
      n /= p

    if n in primes:
      return n

  return curr

print(f'math res: {res(600851475143)}')
