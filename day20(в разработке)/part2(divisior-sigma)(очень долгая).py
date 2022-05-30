#Функция делителей (DivisorSigma)
def sumer(n, x):
    SUM = 1
    if x*50 < n:
        x += 1
    for i in range(x,x+100):
        p = i
        while (n % i == 0):
            n = n // i
            p *= i
        SUM *= (p - 1)//(i - 1)
    return SUM, x                   
                                         
with open('input.txt', 'r') as INPUT:
     house = int(INPUT.readline())//11

presents = 0
counter = 0
x = 2
while presents < house:
    counter += 1
    presents, x = sumer(counter, x)
    if counter%50000 == 0:
        print(counter, ': ', presents, sep = '')

print('Дом #', counter, ': ', presents*11, ' подарков', sep = '')

with open('output2.txt','w') as OUTPUT:
    OUTPUT.write(str(counter))
input()
