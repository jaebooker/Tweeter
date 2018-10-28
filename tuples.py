from histogram import *
def make_tuple_histo(histogram):
    new_tuple_list = []
    for i in histogram:
        new_tuple_list.append((i, histogram[i]))
    new_tuple_list.sort()
    return new_tuple_list
