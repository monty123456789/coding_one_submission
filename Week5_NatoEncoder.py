alphabet1 = {'a': 'alpha', 'b': 'beta', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'xray', 'y': 'yankee', '0': 'zero', '1': 'one', '2': 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7:' seven', 8: 'eight', 9: 'nine',}

word1 = input('enter a word: ')
word3 = input('enter a word: ')

word2 = ''

for letter in word1:
    if letter in alphabet1.keys():
    	word2 += alphabet1.get(letter) + ' '
	#how i did it first

print(word2)       



