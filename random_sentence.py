from random_spinner import *
from histogram import *
from fisher import *
import random
def random_word_from_histogram(histogram):
    n = random.randrange(0,len(histogram))
    return histo_array[n][1]
def stochastic_random_word(histogram):
    for i in range(0,len(histogram)):
        n = random.randrange(0,len(histogram))
        random_number = random.randrange(0,100)
        if (histogram[n][0]/100) > (random_number/100):
            return histogram[n][1]
