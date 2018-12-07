#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Animal(object):
    pass

# 哺乳类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyabble(object):
    def fly(self):
        print("Flying...")