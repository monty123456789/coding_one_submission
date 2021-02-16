word3 = input('enter a word: ').lower()
shift3 = int(input('enter a number: '))


alphab = 'abcdefghijklmnopqrstuvwxyz'
def funct3(word, shift):
    for x in word:
        if x in alphab:
            position = alphab.find(x)
            value = position + shift
            if value > 25:
                value = value % 26
        new_word = alphab[value]
    
        print(new_word, end = '')
funct3(word3, shift3)
