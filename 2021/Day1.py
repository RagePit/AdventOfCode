lines = open('Day1.txt').read().splitlines()

#part 1
inc = -1
last = 0
for line in lines:
    l = int(line)
    if l > last:
        inc += 1
    last = l
print(inc)

#part 2

inc = -1
last = 0

for i, line in enumerate(lines[2:]):
    c = int(line)
    c1 = int(lines[i-1+2])
    c2 = int(lines[i-2+2])
    sum = c + c1 + c2
    if sum > last:
        inc += 1
    last = sum


print(inc)