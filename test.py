"""

1. "Por favor, introduzca una puntuación de 1 a 5. Introduzca '6' para salir".

2. Recibe los puntos de evaluación introducidos en input().

3. Si se introduce una entrada no numérica, se emite "Por favor, introduzca un número" y se entra en el modo de entrada; si se introduce un 6, se emite "Salir" y se termina el programa.

4. Recibe los comentarios introducidos mediante input().

5. Escriba los puntos de evaluación y los comentarios como "Sus puntos: ○ Sus comentarios: XXX".

6. Volver a la 1.

"""
while True:
    try:

        puntuacion = int(input("Por favor, introduzca una puntuación de 1 a 5. Introduzca '6' para salir: "))


        if puntuacion == 6:
            print("Salir")
            break
        

        elif 1 <= puntuacion <= 5:

            comentarios = input("Por favor, introduzca sus comentarios: ")


            print(f"Sus puntos: {puntuacion} Sus comentarios: {comentarios}")
        
        else:
            print("Por favor, introduzca una puntuación válida entre 1 y 5.")
    
    except ValueError:
        print("Por favor, introduzca un número.")