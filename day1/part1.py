import time as t
import sys
class SomeException(BaseException):
    None

class FinalException(BaseException):
    def __init__(self, j = None):
        with open('output1.txt', 'w') as O:
            O.write(str(j))
        print('Ура! Мы смогли вычислить, что Санта дойдёт до {} этажа.'.format(j))
        t.sleep(5)
        while True:
            print('Попробуете ещё раз?')
            Vote = input('(Да/Нет): ')
            print()
            if Vote.lower() == 'да':
                print('\n')
                break
            elif Vote.lower() == 'нет':
                print('\n')
                print('Спасибо за помощь Санте! До встречи в следующем году! Хоу-хоу-хоу...')
                t.sleep(5)
                sys.exit(1)       
            else:
                print('*Санта пытается понять, что Вы сказали, но лишь вопросительно смотрит на Вас.* \n')   
class EndException(BaseException):
    None
    


print('Хоу-хоу-хоу, уже готов помочь Санте? Что ж, приступим!\n')
t.sleep(2)

while True:
    try:
        FloorUp = 0
        FloorDown = 0

        text = input('Введите ТАЙНОЕ сообщение для Санты (или "1" для проверки задания): ')
        if text == '1':
            with open('input.txt', 'r') as I:
                FloorUp = 0
                FloorDown = 0
                k = 0
                for i in I:
                    for j in range(len(i)):
                        if i[j] == '(':
                            FloorUp += 1
                        elif i[j] == ')':
                            FloorDown +=1
                        else:
                            print('*Санта качает головой, не понимая, что ты имеешь в виду*\n')
                            raise SomeException()
        else:
            FloorUp = text.count('(')
            FloorDown = text.count(')')
            if len(text) == (FloorUp + FloorDown):
                raise FinalException(FloorUp - FloorDown)
            else:
                print('*Санта качает головой, не понимая, что ты имеешь в виду*\n')
                raise SomeException()
        Expression = FloorUp - FloorDown
        raise FinalException(Expression)
    
    except SomeException:
        continue
    except FinalException:
        None          
    except EndException:
        break

print('Спасибо за помощь Санте! До встречи! Хоу-хоу-хоу...')
t.sleep(5)
sys.exit(1)
        
        
    
