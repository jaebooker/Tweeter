from __future__ import division
import time

def random_spinner(min_range, max_range):
    time_add = (min_range + max_range) / 100
    start_point = min_range
    end_point = max_range
    start_time = time.time()
    while (time.time()-start_time) < 0.00011:
        if start_point < max_range:
            start_point += time_add
        else:
            start_point = min_range
    start_time = time.time()
    while (time.time()-start_time) < 0.00011:
        if end_point > min_range:
            end_point -= time_add
        else:
            end_point = max_range
    return (start_point+end_point)/2
