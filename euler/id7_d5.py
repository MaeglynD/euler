import math

# if this is anywhere close to an efficent answer then the human race is doomed.
def primes_up_to_n(n):
  primes = [2]
  i = 1

  while len(primes) < n:
    i+=2
    is_prime = True 

    for p in primes:
      if i%p == 0:
        is_prime = False
        break

    if is_prime:
      primes.append(i)
  
  return primes

def res():
  return 0

def brute(n):
  return primes_up_to_n(n)[-1]

print(f'brute res: {brute(10001)}')
# print(f'math res: {res()}')
