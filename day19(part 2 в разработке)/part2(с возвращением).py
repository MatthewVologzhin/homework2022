print('Изучаем разные варианты построения молекулы...')

with open('input.txt','r') as INPUT:
    array = []
    for line in INPUT:
        line = line.strip()
        if '=>' in line:
            line = line.replace(' =>','')
            line = line.split(' ')
            array.append(line)
        else:
            main_moleculs = line
array.sort(key=lambda x: len(x[1]), reverse = True)

def minimize(moleculs, array):
    for trans in array:
        if trans[1] in moleculs:
            pos = moleculs.find(trans[1])
            moleculs = moleculs[:pos] + trans[0] + moleculs[pos + len(trans[1]):]
    if moleculs == 'e':
        return moleculs
    else:
        raise ZeroDivisionError
minimize(main_moleculs, array)

