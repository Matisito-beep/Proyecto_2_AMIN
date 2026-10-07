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

def seleccionar_siguiente_ciudad(ciudad_actual, ciudades_pendientes, feromona, heuristica, alfa, beta, q0):
    if np.random.random() < q0:
        mejor_ciudad = -1
        max_valor = 0
        for c in ciudades_pendientes: 
            valor = (feromona[ciudad_actual][c] ** alfa) * (heuristica[ciudad_actual][c] ** beta)
            if valor > max_valor:
                max_valor = valor
                mejor_ciudad = c
        return mejor_ciudad
    else:
        valores= []
        for c in ciudades_pendientes:
            val = (feromona[ciudad_actual][c] ** alfa) * (heuristica[ciudad_actual][c] ** beta)
            valores.append(val)

        suma_valores = sum(valores)
        if suma_valores == 0:
            return np.random.choice(ciudades_pendientes)

        probabilidades = [v/suma_valores for v in valores]

        siguiente = np.random.choice(ciudades_pendientes, p = probabilidades)
        return siguiente

def construir_ruta_hormiga(num_ciudades, feromona, heuristica, alfa, beta, q0):
    ciudad_inicial = np.random.randint(0, num_ciudades)
    ruta = [ciudad_inicial]

    ciudades_pendientes = list(range(num_ciudades))
    ciudades_pendientes.remove(ciudad_inicial)

    ciudad_actual = ciudad_inicial
    while ciudades_pendientes:
        siguiente_ciudad = seleccionar_siguiente_ciudad(ciudad_actual, ciudades_pendientes, feromona, heuristica, alfa, beta, q0,)
        ruta.append(siguiente_ciudad)
        ciudades_pendientes.remove(siguiente_ciudad)
        ciudad_actual = siguiente_ciudad

    return ruta

def actualizacion_local_feromona(ciudad_i, ciudad_j, feromona, rho, tau_0):
    feromona[ciudad_i][ciudad_j] = (1.0 - rho) * feromona[ciudad_i][ciudad_j] + rho * tau_0
    feromona[ciudad_j][ciudad_i] = feromona[ciudad_i][ciudad_j]
    return