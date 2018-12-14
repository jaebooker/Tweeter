import re
import random
from markov import *
from markov2 import *
#from flask import Flask
#from histogram import *
#from random_sentence import *
# app = Flask(__name__)
#
# @app.route("/")
with open('./stirner.txt') as w:
    stirner_text = w.read()
with open('./trends.txt') as w:
    trend_text = w.read()
trend_list = trend_text.split()
trend_word = trend_list[random.randrange(0,len(trend_list))]
word_list = re.split("\W*[^\'\w+\']", stirner_text)
#holmes_sentence = markdown(word_list, 20)
stirner_sentence = markdown2(word_list, 20)
stirner_string = ""
for i in stirner_sentence:
    stirner_string += " "
    stirner_string += i.lower()
print(trend_word + stirner_string)
