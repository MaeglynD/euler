import math

def f(x):
  return x//2 if x%2==0 else (3*x)+1

def brute():
  seen=set([1])
  mem=[i for i in range(int(1e6))]
  idxs=[i+2 for i in range(int(1e6)-2)]

  while len(idxs) > 1:
    next_idxs = []

    for j in idxs:
      old = mem[j]
      mem[j] = f(mem[j])

      if mem[j] in seen:
          seen.add(old)
      else:
        next_idxs.append(j)

    idxs = next_idxs
  
  return idxs[0]

def res():
  return 0

# print(f'math res: {res()}')
print(f'brute res: {brute()}')
