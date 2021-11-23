# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 01:11:18 2021

@author: 1
"""
#лекция 5 Задание 1 Задание функции, работа со списком
def old_man ():
    Group=[['Петров', 1988,10,2, 175, 80],
           ['Сидоров', 1993,4,2, 193, 100],
           ['Попов', 2001,12,21, 166, 70]]
    
     
    year=Group[0][1] # год рождения Первого
    for x in [1,2]:    
        y=Group[x][1]
        if year < y:
            year =y
            man=Group[x][0]
    print (man,year)
old_man()


#лекция 5 Задание 2 Работа над словарем
def high_man ():
    Group = {'Иванов':{'год рождения' : 1988, 'рост' : 175,  'вес' : 80},     
            'Сидоров':{'год рождения' : 1983, 'рост' : 196,  'вес' : 100}, 
            'Попов':{'год рождения' : 2003, 'рост' : 166,  'вес' : 70}} 

        
    key0 ='Иванов'
    key01 ='год рождения'
    key02 = 'рост'
    key03 = 'вес'
    
 
    height = Group[key0][key02] 
    for key in Group:
        if Group [key][key02] > height:
            height = Group [key][key02]                        
            print ("самый высокий студент" , key, "его рост", height, "cм") 
high_man()              


#Урок 5 задание 3 нечеткое сравнение элементов


def compare(S1, S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count/max(len(S1), len(S2))


Group=[['Петров', 1988,10,2, 175, 80],
       ['Сидоров', 1993,4,2, 193, 100],
       ['Попов', 2001,12,21, 166, 70]]


S1 = Group[0][0]
S2 = Group[2][0]
c = compare (S1, S2)   
print (c, S1, S2)


