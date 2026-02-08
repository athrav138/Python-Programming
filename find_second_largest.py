def find_second_largest(numbers):
  return sorted(set(numbers))[-2]

print("Second largest in the list: ",find_second_largest([1,5,23,-23,4223,232]))