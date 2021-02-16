text = input('Enter a string: ')
for i in set(text):
    #if i in set(alphabet):
    x = text.count(i)   
    y = str(i) + ' appears ' + str(x) + ' times'

    print(y)
