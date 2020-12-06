import re

num = 0

with open('4-input.txt', 'r') as f:
    fields = {'ecl': False, 'pid':False, 'eyr':False, 'hcl':False, 'byr':False, 'iyr':False, 'hgt':False}

    for line in f:
        if line == '\n':
            valid = True
            print(fields)
            for key, val in fields.items():
                if not val:
                    print('missing', key)
                    valid = False
                    break

            if valid:
                print('Valid detected')
                num += 1

            fields = {'ecl': False, 'pid':False, 'eyr':False, 'hcl':False, 'byr':False, 'iyr':False, 'hgt':False}

        else:
            f = line.split(' ')
            keys = [t.split(':')[0] for t in f]
            vals = [t.split(':')[1] for t in f]


            for i, key in enumerate(keys):
                val = vals[i].strip()

                if key == 'byr' and 1920 <= int(val) <= 2002:
                    fields[key] = True
                elif key == 'iyr' and 2010 <= int(val) <= 2020:
                    fields[key] = True
                elif key == 'eyr' and 2020 <= int(val) <= 2030:
                    fields[key] = True
                elif key == 'hgt' and val[-2:] == 'cm' and 150 <= int(val[:-2]) <= 193:
                    fields[key] = True
                elif key == 'hgt' and val[-2:] == 'in' and 59 <= int(val[:-2]) <= 76:
                    fields[key] = True
                elif key == 'hcl' and re.fullmatch(r'#[0-9,a-f]{6}', val):
                    fields[key] = True
                elif key == 'ecl' and (val == 'amb' or val == 'blu' or val == 'brn' or val == 'grn' or val == 'hzl' or val == 'oth' or val =='gry'):
                    fields[key] = True
                elif key == 'pid' and len(val) == 9 and val.isdigit():
                    fields[key] = True

            print(fields)

    for key, val in fields.items():
        if not val:
            valid = False
            break

    if valid:
        num += 1

print(num)
