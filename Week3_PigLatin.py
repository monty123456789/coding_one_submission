vowels = ('a', 'e', 'i', 'o', 'u', 'y')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')


word1 = input('enter a word: ')

def pig_latin(word):
    if word[0] in vowels:
        print(word + 'yay')
    elif word[0] in consonants and word[1] in vowels:
        first_letters = word[0:1]
        word_w_first = word[1:]
        new_word = word_w_first + first_letters + 'ay'
        print(new_word)
    elif word[0:1] in consonants and word[2] in vowels:
        first_letters = word[0:2]
        word_w_first = word[2:]
        new_word = word_w_first + first_letters + 'ay'
        print(new_word)
    elif word[1:2] in consonants:
        first_letters = word[0:3]
        word_w_first = word[3:]
        new_word = word_w_first + first_letters + 'ay'
        print(new_word)
pig_latin(word1)
