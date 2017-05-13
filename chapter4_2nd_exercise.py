grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print("")

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

print(count.keys())
print(count)


