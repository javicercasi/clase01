import copy
class Sudoku():

    
    def __init__(self):
        self.is_playing = True
        self.matriz = []
        self.fijos = []

        
    def string_converter(self,tabla):
        #Este metodo chequeara las posiciones de los valores fijos
        large=len(tabla)
        for i in range (large):
            self.matriz.append(list(tabla[i]))
        print(matriz)
   
        for i in range (9):
            for j in range (9):
                if  self.matriz [i][j] == "x":
                    self.fijos.append

    def chequeo

    '''
    



