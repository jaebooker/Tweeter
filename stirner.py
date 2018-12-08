import re
from mark import *
from markdown_mark2 import *
#from flask import Flask
#from histogram import *
#from random_sentence import *
# app = Flask(__name__)
#
# @app.route("/")
with open('./stirner.txt') as w:
    stirner_text = w.read()
word_list = re.split("\W*[^\'\w+\']", stirner_text)
#holmes_sentence = markdown(word_list, 20)
stirner_sentence = markdown2(word_list, 50)
stirner_string = ""
for i in stirner_sentence:
    stirner_string += " "
    stirner_string += i
print(stirner_string)
