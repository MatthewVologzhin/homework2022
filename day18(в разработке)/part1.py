def switch(array):
  ###############
            if array[i+dot] == 1 and i+dot not in extra_dots:
                counter += 1
            elif i in extra_dots
        if array[i][2] == 1:
            if counter == 2 or counter == 3:
                new_array.append(array[i])
            else:
                new_array.append([array[i][0],array[i][1],0])
        elif array[i][2] == 0:
            if counter == 3:
                new_array.append([array[i][0],array[i][1],1])
            else:
                new_array.append(array[i])
    return new_array

with open('input.txt','r') as INPUT:
    info_array = []
    array = []
    switcher = None
    for line in INPUT:
        string = line.replace('\n', '')
        array.append(string)
    string = array

#Создаём вектор-массив данных о точке
    j = -1
    for element in string:
        j += 1 
        for i in range(len(element)):
            if element[i] == '#':
                switcher = 1
            else:
                switcher = 0
            info_array.append([i,j,switcher])
array = info_array
print(array)

for i in range(1):
    array = switch(array)
    print(array)
    counter = 0
    for element in array:
        if element[2] == 1:
            counter += 1
    print(counter)

    
