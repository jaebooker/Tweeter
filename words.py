import random
from monty import *
from WhatTheFoxSay import *
from fisher import *
from randomdict import *

if __name__ == '__main__':
    quote = random_python_quote()
    what_the_fox_say(quote)
    what_the_fox_say(random_word_generator(5))
    print(fisher_python(["words", "notwords", "wordy", "worthy"]))
