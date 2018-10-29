from random_spinner import *

def fisher_python(words):
  m = len(words)
  while (m):
    m -= 1
    i = random_int_spinner(0,m)
    t = words[m]
    words[m] = words[i]
    words[i] = t
  return words

words = ["Blue", "One", "Fish", "Red"]
print(fisher_python(words))
