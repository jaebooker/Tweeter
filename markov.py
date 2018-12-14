import random
def markdown(word_list, sentence_length):
    chain = []
    random_number = random.randrange(0,len(word_list))
    random_next_word = word_list[random_number]
    chain.append(random_next_word)
    for i in range(0, sentence_length):
        next_word = markdown_unchained(word_list, random_next_word)
        if next_word:
            chain.append(next_word)
            random_next_word = next_word
        else:
            return chain
    return chain

def markdown_unchained(word_list, random_next_word):
    unchained = []
    for i in range(0,len(word_list)):
        if random_next_word == word_list[i]:
            if i == len(word_list)-1:
                break
            unchained.append(word_list[i+1])
    if unchained:
        random_index = random.randrange(0,len(unchained))
        next_word = unchained[random_index]
        return next_word
    else:
        return None

# wlist = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'pasta']
# print(markdown(wlist, 10))
