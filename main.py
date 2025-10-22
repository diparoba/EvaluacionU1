#Creando variables
num_uno = int(input("Ingrese el primer numero")) #int me sirve para especificar que el contenido se convertira en un número entero
num_dos = int(input("Ingrese el segundo numero"))
print(f"""
Menu
1. Suma
2. Resta
3. Multiplicacion
4. Division 
""")
option = input("Ingrese una opcion ")
if option == "1":
    print(f"""
El resultado de {num_uno} más {num_dos} es {num_uno+num_dos}
""")