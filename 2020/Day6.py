f = open('Day6.txt','r').read()

groups = f.split('\n\n')

total = 0
for group in groups:
    answers = group.replace('\n','')
    counts = []
    for answer in answers:
        if answers.count(answer) == len(group.split('\n')):
            if not answer in counts: counts.append(answer)
    total += len(counts)
print(total)