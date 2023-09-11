import unittest
import os
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    def test_NumeroBinario_01(self):
      valor_test = ch.numeroBinario(5)
      valor_esperado = 101
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroBinario_02(self):
      valor_test = ch.numeroBinario(255)
      valor_esperado = 11111111
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroBinario_03(self):
      valor_test = ch.numeroBinario(-10)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)
    
    def test_dividirMultiplicar_01(self):
      valor_test = ch.dividirMultiplicar([2,3,8,12,1,-9, 4,-12,-4])
      valor_esperado = [6, 4, 3, 2, 1, 1, -8, -18, -24]
      self.assertEqual(valor_test, valor_esperado)
    
    def test_dividirMultiplicar_02(self):
      valor_test = ch.dividirMultiplicar([2,4,1,-3])
      valor_esperado = [2, 1, 1, -6]
      self.assertEqual(valor_test, valor_esperado)
    
    def test_crearDiccionario_01(self):
      valor_test = ch.crearDiccionario([16,64,2,1,11,1,5,6,10,4,14,7,8,33])
      valor_esperado = {'multiplos3': [6, 33],
      'cuadrados': [256, 4096, 4, 1, 121, 1, 25, 36, 100, 16, 196, 49, 64, 1089],
      'menores_promedio': [2, 1, 11, 1, 5, 6, 10, 4, 7, 8]}
      self.assertEqual(valor_test, valor_esperado)

    def test_crearDiccionario_02(self):
      valor_test = ch.crearDiccionario([3,6,7,12])
      valor_esperado = {'multiplos3': [3, 6, 12],
      'cuadrados': [9, 36, 49, 144],
      'menores_promedio': [3, 6]}
      self.assertEqual(valor_test, valor_esperado)
    
    def test_trianguloRectangulo_01(self):
      valor_test = ch.trianguloRectangulo(3,3,3)
      valor_esperado = False
      self.assertEqual(valor_test, valor_esperado)

    def test_trianguloRectangulo_02(self):
      valor_test = ch.trianguloRectangulo(3.3,3.3,3.3)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_trianguloRectangulo_03(self):
      valor_test = ch.trianguloRectangulo(3,4,5)
      valor_esperado = True
      self.assertEqual(valor_test, valor_esperado)
    
    def test_ciudadesPoblacion(self):
      ciudades = {
      'São Paulo': 21048514,
      'Buenos Aires': 14975587,
      'Río de Janeiro': 11902701,
      'Bogotá': 10777931,
      'Lima': 10479899,
      'Santiago de Chile': 7112808,
      'Belo Horizonte': 6006091,
      'Caracas': 5622798,
      'Brasília': 4291577
      }
      valor_test = ch.ciudadesPoblacion(ciudades)
      valor_esperado = [['Buenos Aires', 14975587],
      ['Bogotá', 10777931],
      ['Belo Horizonte', 6006091],
      ['Brasília', 4291577],
      ['promedio', 9012796.5]]
      self.assertEqual(valor_test, valor_esperado)
    
    def test_ordenarPalabras_01(self):
      valor_test = ch.ordenarPalabras('saco libro casa')
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_ordenarPalabras_02(self):
      valor_test = ch.ordenarPalabras('Hola-Mundo-Amigo')
      valor_esperado = 'Amigo-Hola-Mundo'
      self.assertEqual(valor_test, valor_esperado)
    
    def test_stringEspejo_01(self):
      valor_test = ch.stringEspejo("Hola Mundo")
      valor_esperado = 'odnuM aloH'
      self.assertEqual(valor_test, valor_esperado)

    def test_stringEspejo_02(self):
      valor_test = ch.stringEspejo("Hoy")
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)


resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))