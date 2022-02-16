import time as t

array = []

with open('input.txt', 'r') as I:
    HMLines = I.readline()

    for line in range(int(HMLines)):
        array.append(I.readline())
    array_2 = (I.readline().split())
    
array = list(map(lambda x: x.strip('\n'), array))
print('Начальные числа: ' + str(array))
print('Последняя строка: ' + str(array_2))

array_3 = []
for i in array_2:
    
    if i in array:
        array_3.append(array.index(i))
    else:
        array_3.append(-1)

print('Позиции чисел последней строки в столбце: ' + str(array_3))

output = open('output.txt', 'w')
for i in range(len(array_3)):
    output.write(str(array_3[i]) + '\n')
output.close()

t.sleep(10)
