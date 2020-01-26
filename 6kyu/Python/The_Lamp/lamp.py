#!/usr/bin/python3

# The Lamp: Revisited
# https://www.codewars.com/kata/570e6e32de4dc8a8340016dd/train/python

class Lamp:
    def __init__(self, color, on=False):
        self.color = color
        self.on = on

    def toggle_switch(self):
        self.on = not self.on

    def state(self):
        if self.on: return "The lamp is on."
        return "The lamp is off."

if __name__ == '__main__':
    L = Lamp("Green")
    print(L.on)
    print(L.color)
    L.toggle_switch()
    print(L.on)
    print(L.state())
    L.toggle_switch()
    print(L.on)
