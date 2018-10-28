from histogram import *
from random_sentence import *
with open('./holmes.txt') as w:
    holmes_text = w.read()
histo_holmes = histogram(holmes_text)
#print(create_sorted_array(histo_holmes))
#print(unique_words(histo_holmes))
#print(frequency("Holmes",histo_holmes))
#print(random_word_from_histogram(histo_holmes))
#print(stochastic_random_word(histo_holmes))
print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = random_word_from_histogram(histo_holmes), word2 = random_word_from_histogram(histo_holmes), word3 = random_word_from_histogram(histo_holmes), word4 = random_word_from_histogram(histo_holmes), word5 = random_word_from_histogram(histo_holmes)))
print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = stochastic_random_word(histo_holmes), word2 = stochastic_random_word(histo_holmes), word3 = stochastic_random_word(histo_holmes), word4 = stochastic_random_word(histo_holmes), word5 = stochastic_random_word(histo_holmes)))
