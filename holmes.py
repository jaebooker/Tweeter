from histogram import *
with open('./holmes.txt') as w:
    holmes_text = w.read()
histo_holmes = histogram(holmes_text)
print(create_sorted_array(histo_holmes))
print(unique_words(histo_holmes))
print(frequency("Holmes",histo_holmes))
