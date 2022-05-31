print('Изучаем разные варианты построения молекулы...')

from random import shuffle,randint
from re import split as spl
import time
import sys
sys.setrecursionlimit(10000)

#Получение данных из "input.txt"
with open('input.txt','r') as INPUT:
    array = []
    for line in INPUT:
        line = line.strip()
        if '=>' in line:
            line = line.replace(' =>','')
            line = line.split(' ')
            array.append(line)
        else:
            main_molecule = line
################################



#Сортировка#
for element in array:
    counter = 0
    for el in element[1]:
        if el.isupper() == True:                  #Считаем кол-во заглавных символов 
            counter += 1
    element.append(counter)
array.sort(key = lambda x: x[2], reverse = True)  #Сортируем список по убыванию заглавных символов

for element in array:                             #Избавляемся от ненужных последних значений кол-ва заглавных символов
    element.remove(element[-1])
############



#Главная функция#
def minimize(molecule, array, last = [],switcher = 0):
    if switcher == 1:              #Переключатель: 1 - если прошёл цикл без изменений
        last1 = last.copy()        #Копирование списка для передачи аргумента без его потери (цикл продолжится с X, а не с 0)
        x = last1[-1][1]  
    elif switcher == 0:            #Если переключатель = 0 - цикл идёт впервые
        x = 0
    else:                          #Условие для непредвиденных обстоятельств со switcher'ом
        print('so intresting...')
    for i in range(x, len(array)): #Цикл, который проходится по индексам трансфораций в array (от X, которая определяется switcher'ом до длины array)
        if switcher == 1:              #Если switcher = 1, то удаляется посленднее значение last и переключатель изменяется на 0
            switcher = 0
            last.remove(last[-1])
            continue
        if array[i][1] in molecule:    #Условие вхождения трансформации в молекулу

            last.append([molecule, i])     #Добавление последнего 1."хорошего" вида молекулы и 2.номер трансформации
            
            n = molecule.find(array[i][1])                                            #| 
            molecule = molecule[:n] + array[i][0] + molecule[n+len(array[i][1]):]     #|   Преобразование молекулы к новому виду
            print(molecule)                                                           #|

            return minimize(molecule, array, last) #Запускаем рекурсию с новыми параметрами
        
    if molecule == 'e':      #Условие, при котором, если возникает молекула с электроном, то возвращается длина "хороших" последовательностей молекул
        return len(last)
    
    switcher = 1             #Если при прохождении цикла не было совпадений с трансформациями, то swticher = 1
    return minimize(last[-1][0], array, last, switcher)  #Рекурсия с новым параметром switcher = 1
#################



a = minimize(main_molecule,array)
print(a)
