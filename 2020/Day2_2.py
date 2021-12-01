list = open('Day2_2.txt').read().splitlines()

# count = 0
# for line in list:
#     t = line.split(' ')
#     limits = t[0].split('-')
#     char = t[1][0]
#     pw = t[2]
#     times = pw.count(char)
#     if times >= int(limits[0]) and times <= int(limits[1]):
#         count+=1
# print(count)


count = 0
for line in list:
    t = line.split(' ')
    positions = t[0].split('-')
    char = t[1][0]
    pw = t[2]
    c=0
    if pw[int(positions[0])-1] == char:
        c+=1
    if pw[int(positions[1])-1] == char:
        c+=1
    if c == 1:
        count+=1
print(count)