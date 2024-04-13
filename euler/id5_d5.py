import math

def res():
  return 0

def primes_up_to_n(n):
  primes = [2]

  for i in range(3, n+1,2):
    is_prime = True

    for p in primes:
      if i%p==0:
        is_prime = False 
        break

    if is_prime:
      primes.append(i)

  return primes 

def brute(n):
  primes = primes_up_to_n(n)
  rec = primes

  for i in range(2, n):
    for j in range(len(primes)):
      p, exp = i, 0

      while p%primes[j]==0:
        p/=primes[j]
        exp+=1
      
      rec[j] = max(rec[j], primes[j]**exp)

  return math.prod(rec)


print(f'brute res: {brute(20)}')
# print(f'math res: {res()}')
