from histogram import *
from fisher import *
def random_word_from_histogram(histogram):
    histo_array = create_sorted_array(histogram)
    fisher_python(histo_array)
    return histo_array[0][1]
