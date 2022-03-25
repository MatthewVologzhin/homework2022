print('Ищем различные возможные комбинации синтезируемых молекул...\n')

with open('input.txt','r') as INPUT:
    moleculs = []
    array_transformation = []
    for line in INPUT:
        line = line.strip()
        if '=>' in line:
            line = line.replace(' =>','')
            line = line.split(' ')
            string = ''
            new_line = []
            for element in line[1]:
                if element.isupper() == True:
                    if string != '':
                        new_line.append(string)
                    string = element
                else:
                    string += element
            new_line.append(string)
            line[1] = new_line
            array_transformation.append(line)
        else:
            moleculs = line
string = ''
moleculs_array = []
for alpha in moleculs:
    if alpha.isupper() == True:
        if string != '':
            moleculs_array.append(string)
        string = alpha
    else:
        string += alpha

array_of_comb = []


for i in range(len(moleculs_array)):
    for j in range(len(array_transformation)):
        mol_copy = moleculs_array.copy()
        if moleculs_array[i] == array_transformation[j][0]:
            mol_copy.pop(i)
            for k in range(len(array_transformation[j][1])):
                mol_copy.insert(i+k, array_transformation[j][1][k])
            if mol_copy not in array_of_comb:
                array_of_comb.append(mol_copy)
print('{} различных молекул мы получит на фузионном реакторе!'.format(len(array_of_comb)))

with open('output1.txt','w') as OUTPUT:
    OUTPUT.write(str(len(array_of_comb)))
    
