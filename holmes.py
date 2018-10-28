from histogram import *
with open('./holmes.txt') as w:
    holmes_text = w.read()
print(histogram(holmes_text))
