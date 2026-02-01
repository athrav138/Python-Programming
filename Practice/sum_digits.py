def sum_digits(n):
  return sum(int(i) for i in str(n))

print(sum_digits(1324))