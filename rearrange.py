import random

quotes = ("Always look on the bright side of life.",
          "You just contradicted me.",
          "No, I didn't!",
          "Yes you did!",
          "THIS... IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]
def random_word_generator(number_input):
    with open('./words.txt') as w:
        rwords = w.read().split()
    random_index = ""
    random_punc = [".","?","!","..."]
    for i in range(0,number_input):
        random_number = random.randint(0, len(rwords) - 1)
        random_word = rwords[random_number]
        if i != number_input-1:
            random_index += str(random_word + " ")
        else:
            new_random_number = random.randint(0, 4)
            random_index += str(random_word + random_punc[new_random_number])
    print(random_index)

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
    random_word_generator(5)
