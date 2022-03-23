from itertools import dropwhile, combinations

with open('input.txt', 'r') as INPUT:
    ingredient_names = []
    new_array = []
    for line in INPUT:
        line = line.replace(':', ' ')
        line = line.replace(',',' ')
        array = line.split()
        ingredient_names.append(array[0])
        array_1 = array.copy()
        for element in array:
            if element.isalpha() == True:
                array_1.remove(element)
        for i in range(len(array_1)):
            array_1[i] = int(array_1[i])
        new_array.append(array_1)
        array_1 = []
array = new_array

numb_array = list(range(101))
perm_numb = list(combinations(numb_array, len(ingredient_names)))
comb_array = []
for element in perm_numb:
    if sum(element) == 100:
        comb_array.append(element)

summa = 0
product_array = []
final_array = []
for element in comb_array:
    product = 1
    array_1 = array.copy()
    for i in range(4):
        for j in range(4):
            array_1[i][j] = element[i]*array_1[i][j]
    for i in range(4):
        for j in range(4):
            summa += array_1[j][i]
        if summa < 0:
            summa = 0
        product_array.append(summa)
        summa = 0
    for x in product_array:
        product *= x
    final_array.append(product)
        


    array_1 = array.copy()
            



print(final_array)

        
        
    
        
        
