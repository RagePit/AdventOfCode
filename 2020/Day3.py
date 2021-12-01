
f = open('Day3.txt','r').read().strip()
map = f.replace('\n','')

cursor = 0

right = 1
down = 2

move = 31 * down + right

count = 0

while True:

    if (cursor % 31) > (30 - right):
        cursor += 31*(down-1) + right
    else:
        cursor += move
    
    if map[cursor] == '#':
        count += 1

    print(count)