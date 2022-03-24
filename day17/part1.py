from itertools import combinations

print('Ищем все возможные решения...\n')

volumes = []
with open('input.txt','r') as INPUT:
    for line in INPUT:
        line = line.strip()
        volumes.append(line)
liters = 150

sum_array = []
for i in range(1,len(volumes)):
    array = list(combinations(volumes, i+1))
    summa = 0
    for element in array:
        for j in range(len(element)):
            summa += int(element[j])
        if summa == liters:
            sum_array.append(element)
        summa = 0

number = len(sum_array)
print('Всего %s способа разлить %d литров напитка!'\
      %(number,liters))
with open('output2.txt','w') as OUTPUT:
    OUTPUT.write(str(len(sum_array)))

    
