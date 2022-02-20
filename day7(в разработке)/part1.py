array = []
def sort(array):
    sorted_array = []
    for element in array:
        if element[0].isdigit():
            sorted_array.append(element)
    new_array = array.copy()
    new_array.remove(sorted_array[0])
    for i in range(len(array)):
        for j in range(len(new_array)):
            if sorted_array[-1][1] == 'OR' or 'AND':
                if new_array[j][0].isdigit():
                    
                    if sorted_array[-1][-1] in new_array[j][2]:
                        sorted_array.append(new_array[j])
                        new_array.remove(sorted_array[-1])
                        break
                elif sorted_array[-1][-1] in new_array[j][0]:
                    sorted_array.append(new_array[j])
                    new_array.remove(sorted_array[-1])
                    break

            elif sorted_array[-1][0] == 'NOT':
                if sorted_array[-1][-1] in new_array[j]:
                    sorted_array.append(new_array[j])
                    new_array.remove(sorted_array[-1])
                    break

            elif sorted_array[-1][1] == 'RSHIFT' or 'LSHIFT':
                if sorted_array[-1][-1] in new_array[j]:
                    sorted_array.append(new_array[j])
                    new_array.remove(sorted_array[-1])
                    break

            elif sorted_array[-1][1] == '->':
                if sorted_array[-1][-1] in new_array[j]:
                    sorted_array.append(new_array[j])
                    new_array.remove(sorted_array[-1])
                    break
    return sorted_array
            

with open('input.txt', 'r') as INPUT:
    for line in INPUT:
        text = line
        text = text[0:-1]
        text = text.split(' ')
        array.append(text)
        if text[0].isdigit():
            start_letter = text[1]
            start_number = text[0]
        #print(text)
    array = sort(array)
    print(array)
 #   for i in range(len(array)):
#       #or
 #       if array[i][1] == 'OR':
  #          array[i][4] = array[i][0] | array[i][2]
   #     elif array[i][1] == 'AND':
    #        array[i][4] = array[i][0] & array[i][2]
     #   elif array[i][0] == 'NOT':
     #       array[i][2] = ~array[i][0]
     #   elif array[i][1] == 'RSHIFT':
     #       array[i][4] = array[i][0] >> array[i][2]
     #   elif array[i][1] == 'LSHIFT':
      #      array[i][4] = array[i][0] << array[i][2]
     #   else:
      #      print('Error!')

