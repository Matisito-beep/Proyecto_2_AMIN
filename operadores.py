import pandas as pd
import numpy as np

def leer_instancia(ruta_archivo):
    matrizCoordenadas = pd.read_table(
        ruta_archivo,
        header=None,
        sep=r'\s+',
        skiprows= 6,
        skipfooter= 2,
        engine= 'python'
    )

    matrizCoordenadas = matrizCoordenadas.drop(columns=0).to_numpy()
    numVariables = matrizCoordenadas.shape[0]

    return matrizCoordenadas, numVariables

def calcular_matriz_distancia(matrizCoordenadas, numVariables):
    matrizDistancias= np.full((numVariables, numVariables), fill_value=-1.0, dtype= float)
    for i in range(numVariables - 1):
        for j in range(i+1, numVariables):
            dist= np.sqrt(np.sum(np.square(matrizCoordenadas[i] - matrizCoordenadas[j])))
            matrizDistancias[i][j]= dist
            matrizDistancias[j][i]= dist
    return matrizDistancias

def evaluar_ruta(ruta, matrizDistancias):
    costo_total = 0
    num_ciudades = len(ruta)
    for i in range (num_ciudades):
        ciudad_actual= ruta[i]
        siguiente_ciudad = ruta[(i+1)% num_ciudades]
        costo_total+= matrizDistancias[ciudad_actual][siguiente_ciudad]
    return costo_total

def inicializar_feromonas(num_ciudades, valor_inicial=1.0):
    matriz_feromona = np.full((num_ciudades, num_ciudades), fill_value = valor_inicial, dtype=float)
    return matriz_feromona

def calcular_heuristica(matriz_distancia, num_ciudades):
    heuristica = np.zeros((num_ciudades, num_ciudades), dtype= float)
    for i in range(num_ciudades):
        for j in range(num_ciudades):
            if i != j and matriz_distancia[i][j] > 0:
                heuristica[i][j] = 1.0/matriz_distancia[i][j]

    return heuristica

def seleccionar_siguiente_ciudad(ciudad_actual):
    return

def construir_ruta_hormiga():
    return

def actualizacion_local_feromona():
    return