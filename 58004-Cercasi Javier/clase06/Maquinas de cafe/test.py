
import unittest
from cafe import (MaquinaBasica, Maquinapremium)


class Test_CafeteraBasica(unittest.TestCase):
    def setUp(self):
        self.cafeB = MaquinaBasica()

    def test_cafe_1(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.cantidadCafe(5), '5g. de cafe')
        self.assertEqual(self.cafeB.cantidadAzucar(0), '0g. de azucar')
        self.assertEqual(self.cafeB.terminado(),'Cafe hecho')                    #(Agregar () en terminado)
        
        #Ahora restare los ingredientes de la maquina:
        self.assertEqual(self.cafeB.nivel_agua,990)
        self.assertEqual(self.cafeB.cant_cafe,95)
        self.assertEqual(self.cafeB.azucar,1000)


    def test_cafe_2(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.cantidadCafe(15), '15g. de cafe')
        self.assertEqual(self.cafeB.cantidadAzucar(3), '3g. de azucar')
        self.assertEqual(self.cafeB.terminado(),'Cafe hecho')

        self.assertEqual(self.cafeB.nivel_agua,990)
        self.assertEqual(self.cafeB.cant_cafe,85)
        self.assertEqual(self.cafeB.azucar,997)
    
    def test_cafe_SinAgua(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(1001),'Disculpe, cantidad de agua no disponible')
        self.assertEqual(self.cafeB.terminado(),'No puedo preparar su cafe')

        self.assertEqual(self.cafeB.nivel_agua,1000)
        self.assertEqual(self.cafeB.cant_cafe,100)
        self.assertEqual(self.cafeB.azucar,1000)

    def test_cafe_SinCafe(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.cantidadCafe(101), 'Disculpe, cantidad de cafe no disponible')
        self.assertEqual(self.cafeB.terminado(),'No puedo preparar su cafe')

        self.assertEqual(self.cafeB.nivel_agua,1000)
        self.assertEqual(self.cafeB.cant_cafe,100)
        self.assertEqual(self.cafeB.azucar,1000)

    def test_cafe_SinAzucar(self):
        self.assertEqual(self.cafeB.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeB.cantidadAgua(10), '10ml de agua')
        self.assertEqual(self.cafeB.cantidadCafe(55), '55g. de cafe')
        self.assertEqual(self.cafeB.cantidadAzucar(1001), 'Disculpe, cantidad de azucar no disponible')
        self.assertEqual(self.cafeB.terminado(),'No puedo preparar su cafe')

        self.assertEqual(self.cafeB.nivel_agua,1000)
        self.assertEqual(self.cafeB.cant_cafe,100)
        self.assertEqual(self.cafeB.azucar,1000)

    def test_cafe_SinMoneda(self):
        self.assertEqual(self.cafeB.sensor_moneda(0), 'Ingrese una moneda')

class Test_CafeteraPremium(unittest.TestCase):

    def setUp(self):
        self.cafeC = Maquinapremium()

    def test_cafe_con_Leche(self):
        self.assertEqual(self.cafeC.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeC.vasoSN(True),'Vaso colocado')
        self.assertEqual(self.cafeC.cantidadAgua(15), '15ml de agua')
        self.assertEqual(self.cafeC.cantidadCafe(10), '10g. de cafe')
        self.assertEqual(self.cafeC.cantidadAzucar(0), '0g. de azucar')
        self.assertEqual(self.cafeC.cantidadLeche(True),'Con leche')
        self.assertEqual(self.cafeC.terminado(),'Cafe hecho')               #(Agregar () en terminado)
        
        #Ahora restare los ingredientes de la maquina:
        self.assertEqual(self.cafeC.nivel_agua,985)
        self.assertEqual(self.cafeC.cant_cafe,90)
        self.assertEqual(self.cafeC.azucar,1000)
        self.assertEqual(self.cafeC.cant_leche,980)

    def test_cafe_sin_Leche(self):
        self.assertEqual(self.cafeC.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeC.vasoSN(True),'Vaso colocado')
        self.assertEqual(self.cafeC.cantidadAgua(13), '13ml de agua')
        self.assertEqual(self.cafeC.cantidadCafe(8), '8g. de cafe')
        self.assertEqual(self.cafeC.cantidadAzucar(5), '5g. de azucar')
        self.assertEqual(self.cafeC.cantidadLeche(False),'Sin leche')
        self.assertEqual(self.cafeC.terminado(),'Cafe hecho')             

        #Ahora restare los ingredientes de la maquina:
        self.assertEqual(self.cafeC.nivel_agua,987)
        self.assertEqual(self.cafeC.cant_cafe,92)
        self.assertEqual(self.cafeC.azucar,995)
        self.assertEqual(self.cafeC.cant_leche,1000)

    def test_sin_vaso(self):
        self.assertEqual(self.cafeC.sensor_moneda(1), 'Procesando, aguarde un momento')
        self.assertEqual(self.cafeC.vasoSN(False),'Vaso no colocado')
        self.assertEqual(self.cafeC.nivel_agua,1000)
        self.assertEqual(self.cafeC.cant_cafe,100)
        self.assertEqual(self.cafeC.azucar,1000)

    












if __name__ == "__main__":
    unittest.main()
