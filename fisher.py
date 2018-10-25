import random

def fisher_python(words):
  m = len(words)
  while (m):
    m -= 1
    i = random.randint(0,m)
    t = words[m]
    words[m] = words[i]
    words[i] = t
  return words
