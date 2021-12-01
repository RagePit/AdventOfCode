import json

list = open('Day1_2.txt').read().splitlines()

for i in list:
    for j in list:
        for k in list:
            sum = int(i) + int(j) + int(k)
            if sum == 2020:
                print(int(i) * int(k) * int(j))