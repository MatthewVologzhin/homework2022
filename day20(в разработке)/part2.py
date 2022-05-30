with open('input.txt', 'r') as INPUT:
     house = int(INPUT.readline())//11

def divisor_sigma(n):
    array = [n//x for x in range(1, 51) if (n%x == 0)]
    return sum(array)

counter = 0
Sum = 0
while Sum < house:
    counter += 1
    Sum = divisor_sigma(counter)
    
print('Дом #', counter, ': ', 11*Sum, ' подарков', sep = '')

with open('output2.txt' , 'w') as OUTPUT:
    OUTPUT.write(str(Sum))
