f = open('Day10.txt','r').read().split()

for num in f:
    f[f.index(num)] = int(num)

f.append(f[-1]+3)

f.sort()

seen = {0:1}

for jolt in f:
    seen[jolt] = 0
    if jolt-1 in seen: seen[jolt] += seen[jolt-1]
    if jolt-2 in seen: seen[jolt] += seen[jolt-2]
    if jolt-3 in seen: seen[jolt] += seen[jolt-3]

print(seen[f[-1]])