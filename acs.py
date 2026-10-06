import sys
import time
import numpy as np
from operadores import (
    leer_instancia,
    calular_matriz_distancia,
    evaluar_ruta
)

def main():
    #Argumentos de la línea de comandos
    
    #Cargar datos 
    ruta_archivo = "datos/berlin52.tsp"
    matriz_coord, num_ciudades = leer_instancia(ruta_archivo)
    matriz_dist = calular_matriz_distancia(matriz_coord, num_ciudades)

    print(f"Instancia cargada. Numero de ciudades: {num_ciudades}")


if __name__ == '__main__':
    main()