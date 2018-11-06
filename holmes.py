from histogram import *
from random_sentence import *
with open('./holmes.txt') as w:
    holmes_text = w.read()
histo_holmes = create_sorted_array(histogram(holmes_text))
fisher_python(histo_holmes)
sum = 200
#print(histo_holmes)
#print(create_sorted_array(histo_holmes))
#print(unique_words(histo_holmes))
#print(frequency("Holmes",histo_holmes))
#print(random_word_from_histogram(histo_holmes))
#print(stochastic_random_word(histo_holmes))
# print(histo_holmes.keys())
print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = histo_holmes[0][1], word2 = histo_holmes[1][1], word3 = histo_holmes[2][1], word4 = histo_holmes[3][1], word5 =histo_holmes[4][1]))
print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = stochastic_random_word(histo_holmes, 0, sum), word2 = stochastic_random_word(histo_holmes, 1, sum), word3 = stochastic_random_word(histo_holmes, 2, sum), word4 = stochastic_random_word(histo_holmes, 3, sum), word5 = stochastic_random_word(histo_holmes, 4, sum)))
print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = stochastic_random_word(histo_holmes, 0, sum), word2 = histo_holmes[1][1], word3 = histo_holmes[2][1], word4 = stochastic_random_word(histo_holmes, 50, sum), word5 = histo_holmes[4][1]))
