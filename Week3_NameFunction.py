first1 = input('Enter your first name: ')
second1 = input('Enter your second name: ')

def name(first, *second):
    print('Hello there ' + first1 + ' ' + second1)
name(first1, second1)
