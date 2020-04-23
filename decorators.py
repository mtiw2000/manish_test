# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:26:21 2020

@author: mtiw2
"""
import functools
import time


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_do_twice



def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1000)

@do_twice
def greet(name):
    print(f"Hello {name}")
    

@do_twice
def return_greeting(name):
    print("creating greeting")
    return(f"Hi {name}")
    

def decorator(func):
    def wrapper_decorator(*args,**kwargs):
        #do something  before
        value = func(*args,**kwargs)
        #do something after
        return value
    
    return wrapper_decorator

