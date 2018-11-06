from __future__ import division
from random_spinner import *
from histogram import *
from fisher import *
import random
def random_word_from_histogram(histogram):
    n = random.randrange(0,len(histogram))
    return histo_array[n][1]
def stochastic_random_word(histogram, i, sum):
    random_number = random.uniform(0,1)
    if (histogram[i][0])/sum > (random_number):
        return histogram[i][1]
    elif i == len(histogram)-1:
        return stochastic_random_word(histogram, 0, sum)
    else:
        return stochastic_random_word(histogram, i+1, sum)
    # for i in range(0,len(histogram)):
    #     n = random.randrange(0,len(histogram))
    #     random_number = random.randrange(0,100)
    #     if (histogram[n][0]/100) > (random_number/100):
    #         return histogram[n][1]
    # for i in range(0,len(histogram)):
    #     n = random_int_spinner(0,len(histogram))
    #     random_number = random_int_spinner(0,100)
    #     if (histogram[n][0]/100) > (random_number/100):
    #         return histogram[n][1]
def spinner_random_word_from_histogram(histogram):
    n = random_spinner(0,len(histogram))
    return histo_array[n][1]
def spinner_stochastic_random_word(histogram):
    for i in random_spinner(0,len(histogram)):
        n = random.random_spinner(0,len(histogram))
        random_number = random_spinner(0,100)
        if (histogram[n][0]/100) > (random_number/100):
            return histogram[n][1]
