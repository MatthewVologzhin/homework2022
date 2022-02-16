import time as t
import sys
class SomeException(BaseException):
    None

class FinalException(BaseException):
    def __init__(self, j = None):
        with open('output2.txt', 'w') as O:
            O.write(str(j))
        print('Ура! Мы смогли вычислить, что Санта дойдёт до подвала на {} шаге.'.format(j))
        t.sleep(5)
class EndException(BaseException):
    None
    


print('Хоу-хоу-хоу, теперь нам предстоит узнать, на каком шаге Санта попадёт ' +
      '\nв подвал! Кто знает, для чего ему это... \nНаверное, там ' +
      'что-то действительно важное или интересное.\n')

while True:
    try:
        FloorUp = 0
        FloorDown = 0

        text = input('Введите ТАЙНОЕ сообщение для Санты (или "0" для проверки задания): ')
        if text == '0':
            with open('input.txt', 'r') as I:
                FloorUp = 0
                FloorDown = 0
                k = 0
                for i in I:
                    for j in range(len(i)):
                        k += 1
                        if i[j] == '(':
                            FloorUp += 1
                        elif i[j] == ')':
                            FloorDown +=1
                            if (FloorUp - FloorDown) == -1:
                                raise FinalException(k)
                        else:
                            raise ZeroDivisionError

        j = 0
        for i in text:
            j += 1
            if i == '(':
                FloorUp += 1
            elif i == ')':
                FloorDown += 1
                if FloorUp - FloorDown == -1:
                    raise FinalException(j)
            else:
                raise ZeroDivisionError

        print('К сожалению, Санте не удастся побывать на -1 этаже в этот раз :c')
        while True:
            print('Попробуете ещё раз?')
            Vote = input()
            if Vote.lower() == 'да':
                print('\n')
                break
            elif Vote.lower() == 'нет':
                print('\n')
                raise EndException()
            else:
                print('*Санта пытается понять, что Вы сказали, но лишь вопросительно смотрит на Вас.* \n')

        
        
            
            
    except ZeroDivisionError:
        print('Решили по-другому шифровать? Увы, Санта ждёт от Вас другой шифр! \n')
    except SomeException:
        continue
    except FinalException:
        break            
    except EndException:
        break

print('Спасибо за помощь Санте! До встречи! Хоу-хоу-хоу...')
t.sleep(5)
sys.exit(1)
        
        
    
