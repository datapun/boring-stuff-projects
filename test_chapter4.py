#spam = [2,4,6,8,10]

#spam[2] = 'hello'
#print(spam)

#print(spam[int(int('3' * 2) // 11)])

spam = ['apples', 'bananas', 'tofu', 'cats','ratatata']

string = ''
for i in range(len(spam)):
    if i == len(spam)-1:
        string = string + 'and ' + spam[i]
    else:
        string = string + spam[i] + ', '

print(string)
