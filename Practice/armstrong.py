def is_armstrong(n):
  n1 = n
  d = [int(n) for n in str(n)]
  sum= 0
  for i in d:
   sum += (pow(i,len(d)))
  return f"The {n1} is the armstrong number" if sum==n1 else f"The {n1} is not a armstrong number"

print(is_armstrong(1593))


"""
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

print(is_armstrong(153))  
"""