import random

quotes = ("Always look on the bright side of life.",
          "You just contradicted me.",
          "No, I didn't!",
          "Yes you did!",
          "THIS... IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]
def random_word_generator():
    with open('./words.txt') as w:
        rwords = w.read().split()
    random_index = []
    for i in range(0,5):
        random_number = random.randint(0, len(rwords) - 1)
        i = rwords[random_number]
        random_index.append(i)
    print("{random_word} {random_word2} {random_word3} {random_word4} {random_word5}!".format(random_word=random_index[0], random_word2=random_index[1], random_word3=random_index[2], random_word4=random_index[3], random_word5=random_index[4]))

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
    random_word_generator()
