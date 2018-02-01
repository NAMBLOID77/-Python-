# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    
    make_square(dave)
    
    turtle.mainloop()

def make_square(dave):
    length = int(raw_input('Tamaño de circulo: '))
    
    for i in range(360):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(1)

if __name__ == '__main__':
    main()
