# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 01:35:13 2021

@author: 1
"""
#Лекция 4 Задание 1 Сумма первых ста чисел
import numpy as np
x=np.array(range(100))
b=np.sum(x)
print(b)

#Лекция 4 Задание 2 Сумма по запросу
txt=int(input("Сумму скольких чисел рассчитать: "))
import numpy as np
x=np.array(range(txt))
b=np.sum(x)
print(b)

#Лекция 4 Задание 3 Среднее любых 100 чисел

import numpy as np
np.random
x=np.random.randint(0, 100, 100)
z= np.mean (x)
print(x, z)