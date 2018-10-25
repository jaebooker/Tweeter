import random

quotes = ("Always look on the bright side of life.",
          "You just contradicted me.",
          "No, I didn't!",
          "Yes you did!",
          "THIS... IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]
