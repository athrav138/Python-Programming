numbers_words = ("zero","one","Two","Three","Four","Five","Six","Seven","Eight","Nine")

n = input("Enter digit: ")

for i in n:
  print(numbers_words[int(i)],end=" ")