print('Изучаем разные варианты построения молекулы...')

from random import shuffle,randint
from re import split as spl

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

def minimize(main, array):
    try:
        while True:
            moleculs = main
            counter = 0
            switcher = 0
            moleculs1 = None
            moleculs2 = 0
            while moleculs1 != moleculs2:
                counter += 1
                shuffle(array)
                for trans in array:
                    if trans[1] in moleculs:
                        moleculs = spl(trans[1], moleculs)
                        print(moleculs)
                        if len(moleculs) == 1:
                            continue
                        A = randint(1,len(moleculs)-1)
                        for i in range(1,2*len(moleculs)-1,2):
                            moleculs.insert(i,trans[1])
                        moleculs[2*A-1] = trans[0]
                        moleculs = ''.join(moleculs)    
                        if moleculs == 'e':
                            print(1)
                            raise ZeroDivisionError
                        break
                if switcher == 1:
                    break
                if moleculs1 == None:
                    moleculs1 = moleculs
                else:
                    moleculs2 = moleculs
                    switcher = 1
    except ZeroDivisionError:
        print(counter)
        print('Nice')
minimize(main_moleculs, array)

