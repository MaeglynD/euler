import math

# sum the squares of the binomial coeff's cus path from origin to vertex along the diagonal
# is bionomial coeff, then square it cus the nxn grid will have the same amount of paths
# backwards. also a symmetry of pascals triangle which would half computation [which indeed
# i am too lazy to add]
def res(n):
  return sum([math.comb(n, k)**2 for k in range(0, n+1)])

def brute():
  return 0

print(f'math res: {res(20)}')
# print(f'brute res: {brute()}')
