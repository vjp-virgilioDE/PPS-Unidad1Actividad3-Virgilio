# Vamos a ver los grafos de flujo para las funciones division y multiplicacion

---

## Grafo de flujo para division

Código de la función:
'''
def division(a, b):
    if b == 0:                  # Nodo 1
        return "Error: División por cero"  # Nodo 2
    return a / b                # Nodo 3
'''

Grafo de flujo:
1.- **Inicio (Nodo 1):** Se evalúa si b==0.
2.- **Camino Verdadero:** Si b==0, se devuelve un mensaje de error (Nodo 2).
3.- **Camino Falso:** Si b!=0, se realiza la división y se retorna el resultado (Nodo 3).

**Diagrama del grafo de flujo:**

'''
       (1) [Inicio]
         |
  b == 0 ?
  /       \\
(Sí)      (No)
(2)      (3)
"Error"   a / b
'''

## Grafo de flujo para multiplicacion

Código de la función:

'''
def multiplicacion(a, b):
    return a * b                # Nodo único
'''

Grafo de flujo:

1.- **Inicio (Nodo 1):** La función simplemente realiza la operación a*b y retorna el resultado.

**Diagrama del grafo de flujo:**

'''
       (1) [Inicio]
         |
     a * b
'''

Estos grafos representan los caminos posibles dentro de las funciones. Para pruebas de caja blanca, es importante asegurar que cada camino sea cubierto por al menos un caso de prueba. En el caso de multiplicacion, el flujo es lineal y directo, mientras que la división hay dos caminos que estarán basados en la evaluación de b == 0.

Se podrían hacer mas controles de la diferentes funciones, tales como ver si a la hora de realizar la llamada a la calculadora podemos introducir un valor que no sea un número o una letra.

Si es un número real o entero... y así con cada funcionalidad.
