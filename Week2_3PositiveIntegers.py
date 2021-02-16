integer1 = int(input('Enter an integer: '))
integer2 = int(input('Enter a second integer: '))
integer3 = int(input('Enter a third integer: '))



for x in range(integer1, integer2 +1):
    y = integer3 / x
    if y % 1 == 0:
        j = x
        print(j)
