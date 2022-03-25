print('Ищем различные возможные комбинации синтезируемых молекул...\n')

from itertools import permutations
import sys
import re
from random import randint
sys.setrecursionlimit(10000)
def minimize(moleculs,array):
    new_arrays = []
    for i in range(len(moleculs)):
        for element in array:
            string = re.sub(element[1],element[0],moleculs[0:randint(-len(moleculs),len(moleculs)):], count=i)
            if string not in new_arrays and string != moleculs:
                new_arrays.append(string)
    if len(new_arrays) > 1:
        for i in range(len(new_arrays)):
            minimize(new_arrays[i],array)
    else:
        print(new_arrays)


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

    moleculs = main_moleculs

numb = minimize(moleculs,array)
print(numb) 
