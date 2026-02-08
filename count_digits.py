def count_digits(num):
  return len(num)

def count_digits1(num):
  count = 0

  while num!=0 :
    count += 1
    num //= 10

  return count


num = input("Enter number: ")
print(f"The number of digits in {int(num)} is:",count_digits(num))
print(f"The number of digits in {int(num)} is:",count_digits1(int(num)))