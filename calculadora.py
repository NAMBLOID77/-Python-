# -*- coding: utf-8 -*-


def run():

    while True:

        command = str(raw_input("""--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [S]umar
            [D]ividir
            [R]estar
            [M]ultiplicar
            [P]otencia
        """))

        if command == 's':
            factor1 = int(raw_input('Escribe tu primer factor a sumar: '))
            factor2 = int(raw_input('Escribe tu segundo factor a sumar: '))
            result = factor1 + factor2
            print('Tu resultado es: {}'.format(result))
        elif command == 'd':
            factor1 = int(raw_input('Escribe tu primer factor a dividir: '))
            factor2 = int(raw_input('Escribe tu segundo factor a dividir: '))
            result = factor1 / factor2
            print('Tu resultado es: {}'.format(result))
        elif command == 'r':
            factor1 = int(raw_input('Escribe tu primer factor a restar: '))
            factor2 = int(raw_input('Escribe tu segundo factor a restar: '))
            result = factor1 - factor2
            print('Tu resultado es: {}'.format(result))
        elif command == 'm':
            factor1 = int(raw_input('Escribe tu primer factor a multiplicar: '))
            factor2 = int(raw_input('Escribe tu segundo factor a multiplicar: '))
            result = factor1 * factor2
            print('Tu resultado es: {}'.format(result))
        elif command == 'p':
            factor1 = int(raw_input('Escribe tu primer factor a multiplicar: '))
            factor2 = int(raw_input('Escribe tu segundo factor a multiplicar: '))
            result = factor1 ** factor2
            print('Tu resultado es: {}'.format(result))



if __name__ == '__main__':
    print('C A L C U L A D O R A')
    run()
