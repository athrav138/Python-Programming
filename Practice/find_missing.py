def find_missing(list,n):
  return  n*(n+1)/2 - sum(list)

print(find_missing([1,2,3,4,8,6,7],8))