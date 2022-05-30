with open('input.txt', 'r') as INPUT:
    min_presents = int(INPUT.readline())

def divisor(n):
    x = 1
    divisions = []
    while True:
        if n % x == 0:
            divisions.append(n / x)
        x += 1
        if x > 50:
            break
    return int(sum(divisions))

for n in range(1, 2*min_presents//11+1):
    if(11 * divisor(n)) >= min_presents:
        house = n
        break
print('Дом #', house, ': ', 11*divisor(n), 'подарков', sep = '')
with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(11*divisor(n)))
