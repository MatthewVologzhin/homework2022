import itertools as perm

string = 'abcdefghijklmnopqrstuvwxyz0123456789'
array = list(perm.product(string, repeat=2))
for i in range(len(array)):
    array[i] = '\\x' + array[i][0] + array[i][1] + '\\'

real_chars = 0
comp_chars = 0
with open('input.txt', 'r') as INPUT:
    for line in INPUT:
        real_chars += len(line)
        line = line.strip()
        line = line[1:-1]
        for element in array:
            if element in line:
                line = line.replace(element, '*')
        if '\\"' in line:
            line = line.replace('\\"','\"')
        if '\\\\' in line:
            line = line.replace('\\\\','\\')
        comp_chars += len(line)

        print(line)
        print(len(line))
print(real_chars - comp_chars)
            
