import math

def res():
  return 0

def is_palindrome(n):
  s = str(n)
  return s[:len(s)//2] == s[-len(s)//2:][::-1]

def brute():
  a, b, mx = 0, 0, 0

  for i in range(999, 100, -1):
    if i*i < mx:
      return [a, b, mx]

    for j in range(i, 100, -1):
      if is_palindrome(i*j):
        a, b = i, j
        mx = max(i*j, mx)
        break

      if i*j < mx:
        break
  
  return mx

# print(f'math res: {res()}')
print(f'brute res: {brute()}')
