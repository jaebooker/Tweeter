import random
import time
from monty import *
from WhatTheFoxSay import *
from fisher import *
from randomdict import *
from random_sentence import *
from histogram import *
import re
stime = time.time()
stringy = "One fishy, two fishy, blue fishy, red fishy"
#words_list = re.split("\W*[^\'\w+\']", stringy)
histo = histogram(stringy)
histofish = create_sorted_array(histo)
fisher_python(histofish)
blank = {}
for i in range(0,100000):
    i = stochastic_random_word(histofish, 0, 9)
    if i not in blank:
        blank[i] = 1
    else:
        blank[i] += 1
print(blank)
if __name__ == '__main__':
    #quote = random_python_quote()
    #what_the_fox_say(quote)
    #what_the_fox_say(random_word_generator(5))
    # print(fisher_python(["words", "notwords", "wordy", "worthy"]))
    # print(random_word_generator(100))
    #print(time.time()-stime)
    pass
