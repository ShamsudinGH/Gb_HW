from random import sample
from examin.new_lesson_7 import press

flag = 0
while True:
    n = 8
    x = sample(range(1, 9), 8)
    y = sample(range(1, 9), 8)
    lis = [(x[i], y[i]) for i in range(8)]
    if press(lis):
        print(lis)
        flag += 1
    if flag == 4:
        break
