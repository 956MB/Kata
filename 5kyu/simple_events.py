#!/usr/bin/env python3

# Simple Events
# https://www.codewars.com/kata/52d3b68215be7c2d5300022f/train/python

class Event():
    def __init__(self):
        self.handlers = []

    def subscribe(self, handler):
        self.handlers.append(handler)
        return self

    def unsubscribe(self, handler):
        self.handlers.remove(handler)
        return self

    def emit(self, *args):
        for handler in self.handlers:
            handler(*args)

if __name__ == '__main__':
    event = Event()

    class Testf():
        def __init__(self):
            self.calls=0
            self.args=[]
        def __call__(self,*args):
            self.calls+=1
            self.args+=args

    f=Testf()

    event.subscribe(f)
    event.emit(1, 'foo', True)
        
    print(f.calls, 1) #calls a handler
    print(f.args, [1, 'foo', True]) #passes arguments
        
    event.unsubscribe(f)
    event.emit(2)
        
    print(f.calls, 1) #no second call
