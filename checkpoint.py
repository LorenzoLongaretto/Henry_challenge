# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def numeroBinario(numero):
    '''
    Esta función recibe como argumento un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    #Tu código aca:
    if not isinstance(numero, int) or numero < 0:
      return None
    else:
      return int(bin(numero)[2:])


def dividirMultiplicar(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar una lista con los siguientes parámetros:
   1.Los números que sean positivos y pares se deben dividir por 2, y el resultado expresado como entero (sin decimales, no redondeando, debe tomar sólo la parte entera de la división por 2).
   2.Los números negativos multiplicados por 2.
   3.Los que no cumplan los criterios anteriores deben quedar igual al valor original.
   4.Ordernar los números de mayor a menor.
   Ej: dividirMultiplicar([2,4,1,-3]): debe retornar: [2, 1, 1, -6]
   '''   
   #Tu código acá
   resultado = []
   for numero in lista:
      if numero > 0 and numero % 2 == 0:
         resultado.append(numero // 2)
      elif numero < 0:
         resultado.append(numero * 2)
      else:
         resultado.append(numero)
   resultado.sort(reverse=True)
   return resultado

def crearDiccionario(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar un diccionario con tres claves, "multiplos3", 'cuadrados", "menores_promedio".
   Para la clave "multiplos3", el valor debe ser una lista con los múltiplos de 3 de la lista original.
   Para la clave "cuadrados", el valor debe ser una lista con los valores de la lista original elevados al cuadrado.
   Para la clave "menores_promedio", el valor debe ser una lista con los valores menores al promedio de la lista original.
   EJ: crearDiccionario([3,6,7,12]): debe retornar: {'multiplos3': [3, 6, 12], 'cuadrados': [9, 36, 49, 144], 'menores_promedio': [3, 6]}
   '''
   #Tu código acá
   diccionario = {}

    # Obtener múltiplos de 3
   multiplos3 = [num for num in lista if num % 3 == 0]
   diccionario["multiplos3"] = multiplos3

    # Obtener cuadrados
   cuadrados = [num ** 2 for num in lista]
   diccionario["cuadrados"] = cuadrados

    # Obtener valores menores al promedio
   promedio = sum(lista) / len(lista)
   menores_promedio = [num for num in lista if num < promedio]
   diccionario["menores_promedio"] = menores_promedio

   return diccionario

# Ejemplo de uso
print(crearDiccionario([3, 6, 7, 12]))
# Salida: {'multiplos3': [3, 6, 12], 'cuadrados': [9, 36, 49, 144], 'menores_promedio': [3, 6]}


def trianguloRectangulo(a,b,c):
   '''
   La función debe recibir como argumentos el valor en cm de los lados de un triángulo (a y b son los catetos), y dado estos valores, retornar True si en efecto corresponden a un triángulo rectángulo, o False en caso contrario. Sólo se debe poder pasar valores enteros como argumentos de la función, caso contrario debe retornar nulo.
   EJ: trianguloRectangulo(3.5,3.5,2.4), debe retornar nulo
   EJ: trianguloRectangulo(3,3,3), debe retornar False
   EJ: trianguloRectangulo(3,4,5), debe retornar True
   '''
   #Tu código acá
   if not all(isinstance(valor, int) for valor in [a, b, c]):
        return None

   lados = [a, b, c]
   lados.sort()

   if lados[0] <= 0 or lados[0] + lados[1] <= lados[2]:
        return False

   if lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2:
        return True

   return False


def ciudadesPoblacion(diccionario):
   '''
   Dado el siguiente diccionario ciudades, la función debe retornar una lista de listas, donde cada elemento de la lista sea una lista con el par ['ciudad', población], pero sólo de las ciudades que comiencen con la letra 'B', y como último elemento de la lista el par ['promedio', promedio de población] con el promedio de población de las ciudades seleccionadas.
   Ej: Si se pidiera ciudades que comiencen con la letra 'S', debe devolver: [['São Paulo', 21048514], ['Santiago de Chile', 7112808],['promedio', 14080661.0]]

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
      Pista: investigar método de string startswith()
   '''
   #Tu código acá
   ciudades_seleccionadas = []
   total_poblacion = 0

   for ciudad, poblacion in diccionario.items():
        if ciudad.startswith('B'):
            ciudades_seleccionadas.append([ciudad, poblacion])
            total_poblacion += poblacion

   promedio_poblacion = total_poblacion / len(ciudades_seleccionadas)
   ciudades_seleccionadas.append(['promedio', promedio_poblacion])

   return ciudades_seleccionadas

def ordenarPalabras(palabras):
   '''
   La función recibe como argumento una secuencia de palabras unidas por guiones, y debe retornar las mismas palabras, unidas por guiones, pero en orden alfabético. Si el argumento que se le pasa no es un string o no contiene guiones, debe retornar nulo.
   EJ: ordenarPalabras('saco-libro-casa') debe retornar 'casa-libro-saco'
   EJ: ordenarPalabras('Hola') debe retornar nulo
   Pista: investigar métodos de string
   '''
   #Tu código acá
   if not isinstance(palabras, str) or '-' not in palabras:
      return None

   palabras_separadas = palabras.split('-')
   palabras_separadas.sort()
   palabras_ordenadas = '-'.join(palabras_separadas)

   return palabras_ordenadas

def stringEspejo(texto):
    '''
    La función recibe como argumento una cadena de texto y retorna la cadena invertida, pero sólo si tiene más de tres caracteres, sino debe retornar nulo.
    EJ: stringEspejo('Hola Mundo') debe retornar 'odnuM aloH'
    EJ: stringEspejo('Hoy') debe retornar nulo
    '''
    #Tu código acá
    if isinstance(texto, str) and len(texto) > 3:
       return texto[::-1]
    else:     
      return None
   
   
# #tests
# #bin
# print(numeroBinario(5)) #101
# print(numeroBinario(255)) #11111111
# print(numeroBinario(-10)) #None
# #divmult
# print(dividirMultiplicar([2,3,8,12,1,-9, 4,-12,-4])) #[6, 4, 3, 2, 1, 1, -8, -18, -24]
# print(dividirMultiplicar([2,4,1,-3])) #[2, 1, 1, -6]
# #diccionario
# print(crearDiccionario([16,64,2,1,11,1,5,6,10,4,14,7,8,33])) #{'multiplos3': [6, 33],
#   #    'cuadrados': [256, 4096, 4, 1, 121, 1, 25, 36, 100, 16, 196, 49, 64, 1089],
#     #  'menores_promedio': [2, 1, 11, 1, 5, 6, 10, 4, 7, 8]}
# print(crearDiccionario([3,6,7,12])) #{'multiplos3': [3, 6, 12],
#     #  'cuadrados': [9, 36, 49, 144],
#   #    'menores_promedio': [3, 6]}
  
# #triangulo
# print(trianguloRectangulo(3,3,3)) #False
# print(trianguloRectangulo(3.3,3.3,3.3)) #None
# print(trianguloRectangulo(3,4,5)) #True
# #ciudades
# ciudades = {
#    'São Paulo': 21048514,
#    'Buenos Aires': 14975587,
#    'Río de Janeiro': 11902701,
#    'Bogotá': 10777931,
#    'Lima': 10479899,
#    'Santiago de Chile': 7112808,
#    'Belo Horizonte': 6006091,
#    'Caracas': 5622798,
#    'Brasília': 4291577
#    }
# print(ciudadesPoblacion(ciudades))  #[['Buenos Aires', 14975587],
#    #   ['Bogotá', 10777931],
#   #    ['Belo Horizonte', 6006091],
#    #   ['Brasília', 4291577],
#    #   ['promedio', 9012796.5]]
   
# #ord palabras
# print(ordenarPalabras('saco libro casa')) #None
# print(ordenarPalabras('Hola-Mundo-Amigo')) #'Amigo-Hola-Mundo'
# #espejo
# print(stringEspejo("Hola Mundo")) #'odnuM aloH'
# print(stringEspejo("Hoy")) #None