f = open('Day9.txt','r').read()
lines = f.split('\n')
nums = []
for line in lines:
    nums.append(int(line))

def getPreamble(index):
    return nums[index-25:index]

def check(number,preamble):
    for num in preamble:
        sub = number - num
        if sub in preamble and sub != num:
            return True
    return False

desired = 0
for i in range(25,len(nums)):
    number = nums[i]
    preamble = getPreamble(i)
    if check(number,preamble) == False:
        desired = number

print(desired)

def doSum(index):
    currentlist = []
    for i in range(index,len(nums)):
        add = nums[i]
        if add == desired: return
        currentlist.append(add)
        sums = sum(currentlist)
        if sums > desired:
            return
        if sums == desired:
            print(min(currentlist)+max(currentlist))


for i in range(0,len(nums)):
    doSum(i)