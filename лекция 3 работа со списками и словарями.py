# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 00:28:04 2021

@author: 1
"""

#лекция 3 Задание 1 Работа над списком 
# Group=[['Петров', 1988,10,2, 175, 80],
#         ['Сидоров', 1993,4,2, 193, 100],
#         ['Попов', 2001,12,21, 166, 70]]


# year=Group[0][1] # год рождения Первого
# for x in [1,2]:    
#     y=Group[x][1]
#     if year < y:
#         year =y
#         man=Group[x][0]
# print (man,year)

#лекция 3 Задание 2 Работа над словарем
Group ={
        'Иванов':{'год рождения' : 1988, 'рост' : 175,  'вес' : 80},     
        'Сидоров':{'год рождения' : 1983, 'рост' : 196,  'вес' : 100}, 
        'Попов':{'год рождения' : 2003, 'рост' : 166,  'вес' : 70}    
        }         
key0 ='Иванов'
key01 ='год рождения'
key02 = 'рост'
key03 = 'вес'

# z=list(Group)
# long=Group[key0][key02] # 
# for key in Group:
#       if Group [key][key02] > long:
#           long = Group [key][key02]
      
             
#           print ("самый высокий студент" , key, "его рост", long, "cм")  

#лекция 3 Задание 3 Запросы
familia=input ("Фамилия студента: ")            
if familia == 'Сидоров': 
    print(Group['Сидоров'])          
if familia == 'Иванов': 
    print(Group['Иванов'])    
if familia == 'Попов': 
    print(Group['Попов'])        