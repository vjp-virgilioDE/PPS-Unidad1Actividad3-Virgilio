""
import mi_modulo

def main():
    print("Ejercicio de cálculadora")
    
  
    while True:
        num1 = input("Introduce el primer número: ")
        num2 = input("Introduce el segundo número: ")
        
        if mi_modulo.isNumber(num1) and mi_modulo.isNumber(num2):
            num1 = float(num1)
            num2 = float(num2)
            break
        else:
            print("Error: Ambos valores deben ser números. Inténtalo de nuevo.")
    
 
    while True:
        print("Selecciona la operación que deseas realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Introduce tu opción (1-5): ")
        
        if opcion == "1":
            print(f"Resultado de la suma: {mi_modulo.suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado de la resta: {mi_modulo.resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado de la multiplicación: {mi_modulo.multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado de la division: {mi_modulo.division(num1, num2)}")
        elif opcion == "5":
            print("Adiós")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    main()
