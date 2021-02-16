given_no = int(input('Enter a number you want to divide: '))
given_div = int(input('Enter a number you want to divide your first number by: '))


def div(given_no, given_div):
      y = given_no
      count = 0
      while given_no >= given_div:
          given_no = given_no - given_div
          count += 1
          if given_no < given_div:
              x = given_no
              print(str(y) + ' divided by ' + str(given_div) + ' is ' + str(count) + ' remainder ' + str(x))

          
div(given_no, given_div)
