import math

def n_primes(n):
  primes = [2,3]

  for i in range(n-2):
    for j in range(primes[-1]+2, primes[-1]**2+1, 2):
      for p in primes:
        if j%p==0:
          break
      else:
        primes.append(j)
        break

  return primes

# I READ THE QUESTION WRONG, BUT THE QUESTION I ANSWERED IS WAY COOLER
# (it just so happens to not work because python is telling me i can't
# multiply the first 500 primes and expect her to store it without yelling)
def res_oops():
  prime_prod = math.prod(n_primes(500))

  for i in range(1, int(1e4)):
    if (n := (-1/2)+math.sqrt(1/4 + 2*prime_prod*i)) % 1.0 == 0:
      return n*(n+1)/2

  return 0

def primes_to_n(n):
  siv = list(range(n+1))

  for i in range(2, int(math.sqrt(n))+1):
    if siv[i]:
      for j in range(i**2, n+1, i):
        siv[j] = 0

  return list(filter(lambda x: x >1, siv))

def res(mx):
  primes = n_primes(50)

  for n in range(7, mx):
    t = (n*(n+1))/2
    tmp = t
    factors = 1

    for p in primes:
      if tmp==1 or factors>500:
        break
      
      acc = 1

      while tmp%p==0:
        tmp/=p
        acc+=1        

      factors*=acc 
    
    if factors > 500:
      return int(t)
  
  return 0

print(res(int(1e6)))

def brute():
  return 0

# print(f'math res: {res()}')
# print(f'brute res: {brute()}')
