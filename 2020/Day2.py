f = open('Day2.txt', 'r').read().splitlines()

big = 0
for line in f:
    arr = line.split(' ')
    nums = arr[0].split('-')
    letter = arr[1][0]
    text = arr[2]

    count = 0
    for char in text:
        if char == letter:
            count += 1
    if count >= int(nums[0]) and count <= int(nums[1]):
        big += 1


print(big)