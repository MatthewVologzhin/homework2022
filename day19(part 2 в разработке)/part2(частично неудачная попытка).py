print('Ищем различные возможные комбинации синтезируемых молекул...\n')

from itertools import permutations
import sys
import re
from random import randint
sys.setrecursionlimit(10000)

def changer(string, trans, counter):
    string_1 = string
    if type(string) == int:
        return string
    
    array = [counter]
    while string_1.find(trans[1]) != -1:
        new_string = string[:string_1.find(trans[1])] + trans[0] + string[string_1.find(trans[1])+len(trans[1]):]
        array.append(new_string)
        string_1 = string_1[:string_1.find(trans[1])] + len(trans[1])*'.' + string_1[string_1.find(trans[1])+len(trans[1]):]
    if len(array) >= 2:
        return array
    elif len(array) == 1:
        None
    elif array[1] == 'e':
        print(array[0])
        return array[0]

    
def minimize(moleculs,array,counter):
    counter += 1
    steps = []
    global sets
    for element in array:
        comb_array = changer(moleculs,element,counter)
        if type(comb_array) == list and len(comb_array) > 2:
            print(comb_array)
            new_comb_array = comb_array
            new_comb_array.pop(0)
            for element_1 in new_comb_array:
                return sets.add(minimize(element_1,array,counter))
    return comb_array

with open('input.txt','r') as INPUT:
    array = []
    for line in INPUT:
        line = line.strip()
        if '=>' in line:
            line = line.replace(' =>','')
            line = line.split(' ')
            array.append(line)
        else:
            main_moleculs = line
array.sort(key=lambda x: len(x[1]), reverse = True)
print(array)


moleculs = main_moleculs
sets = set()
trash_array = []
smth = minimize(moleculs,array,0)
print(sets)
input()
