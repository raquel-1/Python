#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    nombre = sys.stdin.readline()

    import sys
    sys.stdout.write("Mensaje para el usuario") 
    sys.stdout.flush() # ¡Importante! Fuerza a que el texto aparezca ya.


    try:
        # código peligroso
    except Exception as e:
        # El mensaje se envía a la tubería de errores
        sys.stderr.write(f"[STDERR] Error: {e}\n")


    sys.stdout.write("Introduce nombre: ")
    sys.stdout.flush()
    # readline() lee hasta que pulsas "Enter"
    respuesta = sys.stdin.readline()
    # ¡CUIDADO! readline() guarda el "Enter" (\n) al final. 
    # Tienes que limpiarlo:
    nombre_limpio = respuesta.rstrip('\n')