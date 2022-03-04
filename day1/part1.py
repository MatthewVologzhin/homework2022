import time as t
import sys

class FinalException(BaseException):
    def __init__(self, j = None):
        with open('output1.txt', 'w') as O:
            O.write(str(j))
        print('Ура! Мы смогли вычислить, что Санта дойдёт до {} этажа.'.format(j))
        t.sleep(5)
        
print('Хоу-хоу-хоу, уже готов помочь Санте? Что ж, приступим!\n')
t.sleep(2)

while True:
    try:
        FloorUp = 0
        FloorDown = 0

        with open('input.txt','r') as INPUT:
            text = INPUT.readlines()
            text = ''.join(text)


        FloorUp = text.count('(')
        FloorDown = text.count(')')
        raise FinalException(FloorUp - FloorDown)
    except FinalException:
        break          

print('Спасибо за помощь Санте! До встречи! Хоу-хоу-хоу...')
t.sleep(5)
        
        
    
