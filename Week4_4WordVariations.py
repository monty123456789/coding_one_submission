words1 = 'comfortable round support machinery'
def word_combo(words):
    for x in words1.split():
        for i in words1.split():
             if i != x:
                 print(i + ' ' + x)
             elif i == x:
                 print(i + ' ' + x)
           
word_combo(words1)
