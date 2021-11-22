# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 00:27:42 2021

@author: 1
"""

#'имя Ольга', 
#'возраст 30 -возвраст 25...35
# младше 20 не старше 20\
# живет на Пушкино ул==Пушкина
# фамилия Ростова - имя ==Ростова
# зовут нташа -имя Наташа

#Работа над словарем

from pprint import pprint
def compare (s1, s2):
    s1, s2 =[s.lower () for s in [s1,s2]]
    ngrams =[s1[i:i+3] for i in range(len(s1))]
    count=0
    for ngram in ngrams:
        count +=s2.count(ngram)
    return count/ max (len(s1), len(s2))    

def int_val (s):
    try:
        return int(s)
    except ValueError:
        return 0

if __name__== '__main__':
    out = []
    for a,b in [
            ('алгоритм', 'алгоритмы' ),
            ('стол', 'столик'),
            ('стол', 'стул'),
    ]:
        out +=[a,b, compare (a,b)]
    print (out)
print ([int_val(s) for s in ['старше', '30', 'но', '101']])                                

from pprint import pprint
class Person:
    def __init__(self, name, age, adress):
        self.name, self.age, self.adress = name, age, adress
        self.key=(name, adress)
    def __repr__(self):
        return "Person ('%s', '%s', '%s')" % (self.name, self.age, self.adress)
    def __eq__(self,obj):
        if type (obj)==Person:
            return 
        elif type (obj)== str:
            return fuzzy_compfrte (obj)
        else:     
            return      

def by_adress (Q):
    Q=Q-ADRESS_WORDS
    W=set(self.adress.split())
    rez[" "]
    for a,b in product (Q, W):
        rez +=[(compare(a.b), a,b)]
    return max (rez) [0]

def by_age (Q):
    q_age = max([int_val(q) for q in Q])
    if 'старше' in Q:
        return q_age<self.age
    if 'младше' in Q:
        return q_age>self.age
    return q_age+5>=self.age>=q_age-5 



ADRESS_WORDS ={'дом', 'улица', 'живет'}
def fuzzy_compfrte (query):
    q=set (query.split())
    score = 0
    for m, a in zip (
            [ADRESS_WORDS, ],
            [by_adress, by_name, by_age]):
        if m & q:
            score += f(q)
    return score > 0,49        
    
lena = Person ("Лена", 19,"Пушкина, 14, 80")     
oleg = Person ('Олег', 34, "Ленского, 10, 11") 
olga =Person ('Ольга', 28, "Онегина, 11, 12") 
nata =Person ('Наташа', 17, "Ростова, 16, 15")  


queries= ['имя Ольга', 
           'возраст 30',
           'фамилия ростова' ,
          'зовут нташа']

people = {
    lena.key: lena,
    oleg.key: oleg,
    olga.key: olga,
    nata.key: nata,
    }

for query, person in queries, people:
    if person == query:
        print((query, person))
from intertools import product
for query, person in product (queries, people.values()):
      if Person == query:        
          from pprint import pprint
          pprint((query, person))




















