def check_palindrome(string):
  if string==string[::-1]:
    print(f"THe {string} is Palindrome")
  else :
    print("THe {string} is not Palindrome")

str = "HeHe"

check_palindrome(str)