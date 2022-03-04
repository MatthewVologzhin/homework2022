import time as t
import sys

class FinalException(BaseException):
    def __init__(self, j = None):
        with open('output2.txt', 'w') as O:
            O.write(str(j))
        print('Ура! Мы смогли вычислить, что Санта дойдёт до подвала на {} шаге.'.format(j))
        t.sleep(5)

    


print('Хоу-хоу-хоу, теперь нам предстоит узнать, на каком шаге Санта попадёт ' +
      '\nв подвал! Кто знает, для чего ему это... \nНаверное, там ' +
      'что-то действительно важное или интересное.\n')

while True:
    try:
        FloorUp = 0
        FloorDown = 0

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
    except ZeroDivisionError:
        print('Санта не окажется в подвале в этот раз!')
        t.sleep(2)
        break
    except FinalException:
        break            

print('Спасибо за помощь Санте! До встречи! Хоу-хоу-хоу...')
t.sleep(5)
