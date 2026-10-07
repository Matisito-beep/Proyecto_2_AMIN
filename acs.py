import sys
import time
import argparse
import numpy as np
from operadores import (
    leer_instancia,
    calcular_matriz_distancia,
    evaluar_ruta,
    inicializar_feromonas,
    calcular_heuristica,
    construir_ruta_hormiga,
    actualizacion_local_feromona
)

def actualizacion_global(feromona, mejor_ruta_glob, mejor_costo_glob, rho):
    num_ciudades = len(mejor_ruta_glob)
    delta_tau= 1.0/mejor_costo_glob

    for i in range(num_ciudades):
        c1 = mejor_ruta_glob[i]
        c2 = mejor_ruta_glob[(i+1)%num_ciudades]
        feromona[c1][c2] = (1.0 - rho) * feromona[c1][c2] + rho *delta_tau
        feromona[c2][c1] = feromona[c1][c2]



def main():
    #Argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description= "Sistema de colonia de hormigas para TSP")
    parser.add_argument("instancia", type=str)
    parser.add_argument("num_hormigas", type=int)
    parser.add_argument("num_iteraciones", type=int)
    parser.add_argument("alfa", type=float)
    parser.add_argument("beta", type=float)
    parser.add_argument("q0", type=float)
    parser.add_argument("rho", type=float)
    parser.add_argument("semilla", type=int)
    parser.add_argument("salida", type=str)
    
    args = parser.parse_args()

    # Semilla aleatoria
    np.random.seed(args.semilla)
    inicio_tiempo = time.time()


    # Leer instancia
    matriz_coord, num_ciudades = leer_instancia(args.instancia)
    matriz_dist = calcular_matriz_distancia(matriz_coord, num_ciudades)

    # Inicio ACS
    tau_0 = 1.0/ (num_ciudades*10000)
    feromona = inicializar_feromonas(num_ciudades, valor_inicial=tau_0)
    heuristica = calcular_heuristica(matriz_dist, num_ciudades)

    mejor_ruta_glob= None
    mejor_costo_glob = float('inf')

    #Bucle
    for iteracion in range(args.num_iteraciones):
        mejor_ruta_iter = None
        mejor_costo_iter = float('inf')
        for _ in range(args.num_hormigas):
            ruta = construir_ruta_hormiga(num_ciudades, feromona, heuristica, args.alfa, args.beta, args.q0)
            costo = evaluar_ruta( ruta, matriz_dist)

            for i in range(num_ciudades):
                c1 = ruta[i]
                c2 = ruta[(i+1)% num_ciudades] 
                actualizacion_local_feromona(c1, c2, feromona, args.rho, tau_0)

            if costo < mejor_costo_iter:
                mejor_costo_iter = costo
                mejor_ruta_iter = ruta

        if mejor_costo_iter < mejor_costo_glob:
            mejor_costo_glob = mejor_costo_iter
            mejor_ruta_glob = mejor_ruta_iter
            print(f"Mejor costo en iteracion: {iteracion+1} Costo: {mejor_costo_glob:.2f}")
        actualizacion_global(feromona, mejor_ruta_glob, mejor_costo_glob, args.rho)

    tiempo_total = time.time() - inicio_tiempo

    print("\n")
    print(f"Mejor costo global encontrado: {mejor_costo_glob:.2f}")
    print(f"Tiempo total de la ejecucion: {tiempo_total:.4f}")
    print(f"Mejor ruta global encontrada: {mejor_ruta_glob}")

if __name__ == '__main__':
    main()