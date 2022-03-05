print('Считаем кредиты, дебеты, 1+1, 2+2=5 для Санты!\n')

with open('input.txt','r') as INPUT:
    string = INPUT.readline()
string = string.replace('\"red\"', '*')

print(string)
while True:
    counter = 0
    end_index_1 = -1
    start_index_1 = -1
    for i in range(len(string)):
        counter += 1
        if string[i] == '{':
            start_index = i
        elif string[i] == '}':
            end_index = i
            if '*' in string[start_index:end_index+1]:
                if start_index_1 != -1 and end_index_1 != -1:
                    if '*' in string[start_index_1:end_index_1+1]:
                        string = string.replace('*','.')
                        break
                else:
                    new_string = string[:start_index] + string[end_index+1:]
        if string[i] == '[':
            start_index_1 == i
        elif string[i] == ']':
            end_index_1 == i
    string = new_string
    print(counter)
    print(len(string))
    if counter == len(string):
        break

for element in string:
    if element.isdigit() == False and element != '-':
        string = string.replace(element, '.')

array = []
new_array = []
array = string.split('.')
for element in array:
    if element != '':
        new_array.append(int(element))


print('Бухгалтерское универсальное число для Санты:', sum(new_array), sep = ' ')

with open('output2.txt','w') as O:
    O.write(str(sum(new_array)))

            
            



        
