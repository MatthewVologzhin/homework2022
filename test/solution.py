# Открываем файл и форматируем его для удобного чтения его программой
with open('input.txt', 'r') as INPUT:
    value = int(INPUT.readline())
    array = []
    for i in range(value):
        array.append(INPUT.readline().split())

#Добавляем в конце каждого кандидата его порядковый номер
counter = 0
for element in array:
    counter += 1
    element.append(counter)
print('Начальная строка:' , array)



#Функция, которая пробегается по всем кандидатам
def deep(array, cand, valuer = [], val_ar = []):

    watcher = cand
    valuer = valuer.copy()
    valuer.append(watcher[2])

    for i in range(len(array)):

        if watcher[1] <= array[i][0] and watcher[2] != array[i][2]:
            deep(array, array[i], valuer, val_ar)
    val_ar.append(valuer)
    return val_ar


#Функция, подчищающая ненужные значения и выводящая наиболее оптимальный порядок выступления
#P.S. Нам важно найти такой порядок, при котором будет затрачено меньше времени и
#     будет выслушено наибольшее число кандидатур
def minimize(array, val_ar):
    Maxs = []
    Max = 1
    for element in val_ar:           #Находим максимальное число кандидатур
        if len(element) > Max: 
            Max = len(element)
    new_array = []
    for element in val_ar:           #Находим выступления с наибольшим числом кандидатов
        if len(element) == Max:
            new_array.append(element)
    val_ar = new_array

    best_time = 0                    #Отсекаем те варианты выступлений, которые являются более длинными
    best = val_ar[0]
    for val in val_ar:               
        duration = 0
        for el in val:
            dur = int(array[el-1][1])- int(array[el-1][0])
            duration += dur

        if duration < best_time:
            best_time = duration
            best = val
    return best
    
    
new_array = []  
for i in range(len(array)):          #Запускаем функцию для каждого начального положения
    a = deep(array, array[1])
    a = minimize(array, a)
    if a not in new_array:
       new_array.append(a)

new_array = new_array[0]             #Преобразуем строку в подлежащий вид
string = ' '.join([str(i) for i in new_array])


print('Наиболее выгодный вариант выступлений:', string)

#Выводи значение строки в файл "output.txt"
with open('output.txt', 'w') as OUTPUT:
    OUTPUT.write(string)


