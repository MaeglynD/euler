import math

def res():
  return sum(map(lambda x: int(x), str(math.factorial(100))))

def brute():
  return 0

print(f'math res: {res()}')
# print(f'brute res: {brute()}')
