import random

quotes = ("Always look on the bright side of life.",
          "You just contradicted me.",
          "No, I didn't!",
          "Yes you did!",
          "THIS... IS AN EX-PARROT!!")
fox_word = ""
#Image below thanks to some guy named Todd Vargo... so thanks, Todd
fox = ["   /\   /\ ","\
  //\\_//\\  _","\
  \_     _/    /   /","\
   / * * \    /^^^]","\
   \_\O/_/    [   ]","\
    /   \_    [   /","\
    \     \_  /  /","\
     [ [ /  \/ _/","\
    _[ [ \  /_/"]
def what_the_fox_say(fword):
    fox_word = fword
    print(fox[0])
    print(fox[1] + fox_word)
    for i in range(2,9):
        print(fox[i])
def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]
def random_word_generator(number_input):
    with open('./words.txt') as w:
        rwords = w.read().split()
    random_index = ""
    random_punc = [".","?","!","..."]
    for x in range(0,number_input):
        random_number = random.randint(0, len(rwords) - 1)
        random_word = rwords[random_number]
        if x != number_input-1:
            random_index += str(random_word + " ")
        else:
            new_random_number = random.randint(0, 3)
            random_index += str(random_word + random_punc[new_random_number])
    return random_index

if __name__ == '__main__':
    quote = random_python_quote()
    what_the_fox_say(quote)
    what_the_fox_say(random_word_generator(5))
