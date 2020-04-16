# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:46:45 2020

@author: mtiw2
"""

def add_one(number):
    return number + 1


def say_hello(name):
    return f"Hello {name} "


def be_awesome(name):
    return f"Yo {name}, together we are awesome"

def greet_bob(greeter_func):
    return greeter_func("Bob")


say_hello('Bob')
greet_bob(say_hello)




def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    first_child()
    second_child()

    return (first_child)


a=parent()

a()



    
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

second()
    

def my_decorator(func):
    def wrapper():
        print('something is happening before function is called')
        func()
        print('something is happening after the function is called')
        
    return(wrapper)


def say_whee():
    print("Whee!")
    

say_whee = my_decorator(say_whee)

say_wee()



    
@my_decorator
def say_wee():
    print('whee')

    

say_wee()



from decorators import do_twice




from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

say_whee()

    
    