import re
from mark import *
from markdown_mark2 import *
#from flask import Flask
#from histogram import *
#from random_sentence import *
# app = Flask(__name__)
#
# @app.route("/")
with open('./holmes.txt') as w:
    holmes_text = w.read()
word_list = re.split("\W*[^\'\w+\']", holmes_text)
#holmes_sentence = markdown(word_list, 20)
holmes_sentence = markdown2(word_list, 50)
holmes_string = ""
for i in holmes_sentence:
    holmes_string += " "
    holmes_string += i
print(holmes_string)
#histo_holmes = create_sorted_array(histogram(holmes_text))
#fisher_python(histo_holmes)
#sum = 200
#print(histo_holmes)
#print(create_sorted_array(histo_holmes))
#print(unique_words(histo_holmes))
#print(frequency("Holmes",histo_holmes))
#print(random_word_from_histogram(histo_holmes))
#print(stochastic_random_word(histo_holmes))
# print(histo_holmes.keys())
#print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = histo_holmes[0][1], word2 = histo_holmes[1][1], word3 = histo_holmes[2][1], word4 = histo_holmes[3][1], word5 =histo_holmes[4][1]))
#print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = stochastic_random_word(histo_holmes, 0, sum), word2 = stochastic_random_word(histo_holmes, 1, sum), word3 = stochastic_random_word(histo_holmes, 2, sum), word4 = stochastic_random_word(histo_holmes, 3, sum), word5 = stochastic_random_word(histo_holmes, 4, sum)))
#print("{word1} {word2} {word3} {word4} {word5}.".format(word1 = stochastic_random_word(histo_holmes, 0, sum), word2 = histo_holmes[1][1], word3 = histo_holmes[2][1], word4 = stochastic_random_word(histo_holmes, 50, sum), word5 = histo_holmes[4][1]))
