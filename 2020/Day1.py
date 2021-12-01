list = open("Day1.txt","r").read().splitlines()

for i in range(0,len(list)):
    for j in range(1,len(list)):
        for k in range(1,len(list)):
            sum = int(list[i]) + int(list[j]) + int(list[k])
            if sum == 2020:
                print(int(list[i]) * int(list[j]) * int(list[k]))
