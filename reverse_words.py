#Reversing the words in the sentence

def reverse_words(sen):
  return " ".join(word[::-1] for word in sen.split())

""" for word in sen.split():
    return "".join(word[::-1])
"""

print(reverse_words("Python is Interpreted Language ."))