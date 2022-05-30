import matplotlib.pyplot as plt

#Для рассмотрения зависимости сумм делителей от их количества
#Просто запустить код и будет показана зависимость для чисел до 10000

def min_house(house_numb):
    array = [x for x in range(1, house_numb//2 + 1) if house_numb%x == 0]
    Sum = 0
    array.append(house_numb)
    for numb in array:
         Sum += numb
    return Sum, len(array)

counter = 0
Summer = list()
lenner = list()
while counter < 10000:
    counter += 1
    a, b = min_house(counter)
    Summer.append((a-counter)//200)
    lenner.append(b)
counter = [x for x in range(1,10001)]

fig = plt.figure()
graph = plt.plot(counter, Summer)
graph2 = plt.plot(counter, lenner)
grid = plt.grid(True)
plt.show()
print(max(Summer))
