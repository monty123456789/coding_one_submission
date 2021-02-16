list = [2, 4, 54, 56]

def multiply(*numbers):
    result = 1
    for x in list:
        result = result * x
        print(result)
multiply(list)
