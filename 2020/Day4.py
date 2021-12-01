f = open('Day4.txt','r').read()

map = f.split('\n\n')

work = 0
for line in map:
    passport = line.replace('\n',' ')
    fields = passport.split(' ')
    count = 0
    for field in fields:
        if field.startswith('cid'):
            continue
        if field.startswith('byr'):
            if int(field[4:8]) < 1920 or int(field[4:8]) > 2002:
                continue
        if field.startswith('iyr'):
            if int(field[4:8]) < 2010 or int(field[4:8]) > 2020:
                continue
        if field.startswith('eyr'):
            if int(field[4:8]) < 2020 or int(field[4:8]) > 2030:
                continue
        if field.startswith('hgt'):
            if not (field.endswith('cm') or field.endswith('in')):
                continue
            num = int(field.replace('hgt:','').replace('cm','').replace('in',''))
            if field.endswith('cm'):
                if num < 150 or num > 193:
                    continue
            if field.endswith('in'):
                if num < 59 or num > 76:
                    continue
        if field.startswith('hcl'):
            color = field.replace('hcl:','')
            if color == 'z':
                continue
            if not color.startswith('#'):
                continue
        if field.startswith('ecl'):
            color = field.replace('ecl:','')
            if color.startswith('#'):
                continue
            if not (color == 'amb' or color == 'blu' or color == 'brn' or color == 'gry' or color == 'grn' or color == 'hzl' or color == 'oth'):
                continue
        if field.startswith('pid'):
            id = field.replace('pid:','')
            if not len(id) == 9:
                continue
        count += 1
    if count >= 7:
        work += 1
print(work)