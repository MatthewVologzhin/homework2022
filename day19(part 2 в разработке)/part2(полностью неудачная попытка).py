print('Ищем различные возможные комбинации синтезируемых молекул...\n')
def sort(array):
    array_of_numb = []
    for element in array:
        counter = 0
        for alpha in element:
            if alpha.isupper() == True:
                counter += 1
        array_of_numb.append(counter)
    array = list(sorted(array,reverse=True))
    return array
from math import ceil
from re import sub 
with open('input.txt','r') as INPUT:
    array = []
    for line in INPUT:
        line = line.strip()
        if '=>' in line:
            line = line.replace(' =>','')
            line = line.split(' ')
            array.append(line)
        else:
            chain = line

#Проанализируем максимальное количество преобразований
score_array = []
for element in array:
    HME = 0
    for alpha in element[1]:
        if alpha.isupper() == True:
            HME += 1
    score_array.append(HME)
average = sum(score_array)/len(score_array)


HME = 0
for element in chain:
    if element.isupper() == True:
        HME += 1
print('Приблизительно {} операций.'.format(ceil(HME/average)))

#Найдём молекулы, которые не имеют превращений вперёд, а только обратно
start_moleculs = []
end_moleculs = []
for element in array:
    if element[0] not in start_moleculs:
        start_moleculs.append(element[0])
    elements = element[1] 
    elements = sub(r'([A-Z])', r'.\1',elements)
    smth = elements.split('.')
    smth.pop(0)
    for element_1 in smth:
        if element_1 not in end_moleculs:
            end_moleculs.append(element_1)
end_moleculs_2 = end_moleculs.copy()
for element in end_moleculs:
    if element in start_moleculs:
        end_moleculs_2.remove(element)
end_moleculs = end_moleculs_2

#Найдём преобразования, в которых как минимум два элемента конечны
new_array = []
for element in array:
    counter = 0
    for atom in end_moleculs:
        if atom in element[1]:
            counter += 1
        if counter > 1 and element[1] not in new_array:
            new_array.append(element[1])

#Отыщем основные структуры, которые будут фигугировать в анализе
struct_array = []
for element in new_array:
    for element_1 in start_moleculs:
        if element_1 in element:
            element = sub(element_1, '.', element)
    if element not in struct_array:
        struct_array.append(element)
struct_array = sort(struct_array)
print('Основные структуры для анализа:', struct_array)

#Выделяем внутренние фрагменты, которые нужно обработать
for struct in struct_array:
    if r'{}'.format(struct) in chain:
        print(True)
