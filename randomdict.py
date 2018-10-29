from random_spinner import *
def random_word_generator(number_input):
    with open('./words.txt') as w:
        rwords = w.read().split()
    random_index = ""
    random_punc = [".","?","!","..."]
    for x in range(0,number_input):
        random_number = random_int_spinner(0, len(rwords)-1)
        random_word = rwords[random_number]
        if x != number_input-1:
            random_index += str(random_word + " ")
        else:
            new_random_number = random_int_spinner(0, 3)
            random_index += str(random_word + random_punc[new_random_number])
    return random_index
