f = open('Day5.txt','r').read().splitlines()

highest = 0
ids = []
for bo in f:
    row = bo[0:7]
    binary = row.replace('F','0').replace('B','1')
    row = int(binary, 2)

    seat = bo[7:10]
    binary = seat.replace('L','0').replace('R','1')
    seat = int(binary, 2)

    ID = row * 8 + seat
    if ID > highest:
        highest = ID
    ids.append(ID)

for num in ids:
    if not num+1 in ids:
        print(num+1)
