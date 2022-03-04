array = []
numb = 0
counter = 0
dict_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

print('Начальные данные в 16-ой системе:')
with open('input.txt', 'r') as INPUT:
    lines = INPUT.readlines()
    for element in lines:
        element = element.strip()
        print(element)
print(' ')
        
print('Конечные данные в 10-ой системе:')
with open('input.txt','r') as INPUT:
    for line in INPUT:
        number = line.strip()
        HL = len(number) - 1
        for element in number:
            if element in dict_16.keys():
                element = dict_16.get(element)
            numb += int(element)*16**(HL)
            HL -= 1
            
        array.append(numb)
        counter = 0
        numb = 0
for element in array:
    print(element)
with open('output.txt','w') as OUTPUT:
    for element in array:
        OUTPUT.write(str(element))

