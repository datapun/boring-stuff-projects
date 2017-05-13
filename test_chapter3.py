def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    elif number%2 == 1:
        print(number*3+1)
        return number*3+1

print('enter a number:')
try:
    numberMain = int(input())
    while numberMain != 1:
        newNumber = collatz(numberMain)
        numberMain = newNumber
    print('hell yeah')
except ValueError:
    print('enter an integer, please!')
