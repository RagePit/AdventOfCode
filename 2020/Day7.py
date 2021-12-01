f = open('Day7.txt','r').read()

lines = f.split('\n')

rules = {}
for line in lines:
    one = line.split(' contain ')
    two = one[1].split(', ')
    one = one[0].replace(' bags','')
    if 'no other bags' in line:
        rules[one] = {}
        continue
    newtwo = {}
    for bag in two:
        amount = int(bag[0])
        id = bag[2:].replace(' bags','').replace('.','').replace(' bag','')
        newtwo[id] = amount
    rules[one] = newtwo


def count(bagid):
    # print(bag_id)
    found = []
    for bag in rules:
        inside = rules[bag]
        if bagid in inside:
            found.append(bag)
            found += count(bag)
    return found

def count2(bagid):
    found = 0
    inside = rules[bagid]
    for bag in inside:
        found += inside[bag]
        found += (inside[bag] * count2(bag))
    return found

print(len(set(count('shiny gold'))))

print(count2('shiny gold'))

