import random
from histogram import *
from fisher import *
def random_word_from_histogram(histogram):
    histo_array = create_sorted_array(histogram)
    fisher_python(histo_array)
    return histo_array[0][1]
def stochastic_random_word(histogram):
    new_histo_array = create_sorted_array(histogram)
    fisher_python(new_histo_array)
    for i in range(0,len(new_histo_array)):
        random_number = random.randrange(0,100)
        if (new_histo_array[i][0]/100) > (random_number/100):
            return new_histo_array[i][1]
