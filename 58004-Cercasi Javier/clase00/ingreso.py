from sudo import Sudoku
#from API import API
#import sys
#import math


class UserInput():
    
    def ingreso_numero(self, number, tamaño):
        if(number > 0 and number <= tamaño):
            return True
        else:
            return False

    def ingreso_coordenadas(self, fila, columna, tamaño):
        if(fila > 0 and fila <= tamaño and columna > 0 and columna <= tamaño):
            return True
        else:
            return False

    

    def dimension(self, tamaño):
        return (tamaño != 4 and tamaño != 9)
    
    def ingresar_dimension(self):
        self.tamaño = 0
        while not self.dimension(self.tamaño):
            try:
                self.tamaño = int(input("Ingrese el tamaño sudoku (4 o 9): "))
                if (self.dimension(tamaño)):
                    return self.tamaño
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
    
    def jugar(self):
        self.dimension() # donde se guarda la dimension???
        # crear sudoku...
        juego = Sudoku()
        while not juego.fin_juego():
            # mostrar tablero
            print(juego.get_board())
            # ingresar ...
            # poner en el sudoku...


if __name__ == "__main__":
    u = UserInput()
    u.play()