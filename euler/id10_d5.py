import math

# eratsothenes, i will resurrect you just to show you my neat
# code of your algorithm you made with sand and sticks.
# where i come from we look at holographic, glass encrusted devices
# and nobody makes friends, we just talk to the glass. 
def brute(n):
  mem = list(range(n+1))

  for i in range(2, int(math.sqrt(n)+1)):
    if mem[i]:
      for j in range(i**2, n+1, i):
        mem[j] = 0 
  
  return sum(mem)-1

def res():
  return 0

print(f'brute res: {brute(int(2e6))}')
# print(f'math res: {res()}')
