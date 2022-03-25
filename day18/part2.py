#Функция изменения массива
def change(array):
    dots = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    corner_dots = [[0,0],[len(array)-1,len(array)-1],[len(array)-1,0],[0,len(array)-1]]
    new_array = [[] for x in range(len(array))]
    for dot in corner_dots:
        array[dot[1]][dot[0]] = '#'
        
    for y in range(len(array)):
        for x in range(len(array[y])):
            counter = 0
            try:
                for dot in dots:
                    if 0 <= x + dot[0] and x + dot[0] <= len(array)-1\
                       and 0 <= y + dot[1] and y + dot[1] <= len(array)-1:

                        if array[y+dot[1]][x+dot[0]] == '#':
                            counter += 1
            except:
                print('Error!')

            if array[y][x] == '#':
                if counter == 2 or counter == 3:
                    new_array[y].append('#')
                else:
                    new_array[y].append('.')
            elif array[y][x] == '.':
                if counter != 3:
                    new_array[y].append('.')
                elif counter == 3:
                    new_array[y].append('#')
    return new_array

print('Просчитываем включения и выключения ламп со сломанными лампами...\n')                
            
#Разделяем массив для удобного чтения
with open('input.txt','r') as INPUT:
    array = []
    for line in INPUT:
        line = line.strip()
        small_array = []
        for element in line:
            small_array.append(element)
        array.append(small_array)

#Запускаем функцию 100 раз
for i in range(100):
    array = change(array)
corner_dots = [[0,0],[len(array)-1,len(array)-1],[len(array)-1,0],[0,len(array)-1]]
count = 0
for dot in corner_dots:
    if array[dot[1]][dot[0]] == '.':
        array[dot[1]][dot[0]] = '#'
for element in array:
    if '#' in element:
        count += element.count('#')
print('Через 100 циклов будет включено {} фонарей с учётом сломанных углов!'.format(count))
with open('output2.txt','w') as OUTPUT:
    OUTPUT.write(str(count))
