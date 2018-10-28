import re
def histogram(words):
    words_list = re.split("(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)", words)
    #thanks to Martijn Pieters for the above split
    word_dictionary = {}
    counter = len(words_list)-1
    i = 0
    while i < counter:
        word_dictionary[words_list[i]] = 1
        n = i+1
        while n < counter:
            if words_list[i] == words_list[n]:
                word_dictionary[words_list[i]] += 1
                words_list.pop(n)
                counter -= 1
            n += 1
        i += 1
    return word_dictionary
def unique_words(histogram):
    return len(histogram)
def frequency(word, histogram):
    return histogram[word]
