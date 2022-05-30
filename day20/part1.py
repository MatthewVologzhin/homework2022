#Функция делителей (DivisorSigma)
def sumer(n):
    SUM = 1
    for i in range(2,50):            #Наибольшее количество множителей получается
        p = i                        #Благодаря меньшим множителям (2,3,5 и т.д.)
        while (n % i == 0):          #Тогда диапазон резонно выставлять не больше ~25
            n = n // i               #Для моего входного числа может использоваться
            p *= i                   #Диапазон от 2 до 12
        SUM *= (p - 1)//(i - 1)      #P.S. Чем БОЛЬШЕ огромных простых чисел, тем МЕНЬШЕ их сумма
    return SUM                       #Ради интереса предлагаю посмотреть как колеблется сумма делителей чисел и как зависит от количества делителей
                                         
with open('input.txt', 'r') as INPUT:
     house = int(INPUT.readline())//10

presents = 0
counter = 0
while presents < house:
    counter += 1
    presents = sumer(counter)

print('Дом #', counter, ': ', presents, ' подарков', sep = '')

with open('output1.txt','w') as OUTPUT:
    OUTPUT.write(str(counter))
