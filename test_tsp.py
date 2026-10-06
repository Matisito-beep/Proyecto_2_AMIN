import os
from operadores import leer_instancia, calcular_matriz_distancia

if __name__ == "__main__":
    # Ruta donde guardaste tu archivo berlin52.tsp
    ruta_archivo = os.path.join("datos", "berlin52.tsp")
    
    print("=" * 55)
    print("      PRUEBA DE LECTURA DE INSTANCIA TSP (Berlin52)")
    print("=" * 55)
    
    try:
        # 1. Probar la lectura de coordenadas
        matriz_coord, num_ciudades = leer_instancia(ruta_archivo)
        print(f"[OK] Archivo leído con éxito desde: {ruta_archivo}")
        print(f"Número total de ciudades detectadas : {num_ciudades}")
        print(f"Dimensiones de la matriz de coords  : {matriz_coord.shape}")
        
        # Verificar contra el archivo original (La ciudad 1 debe ser x=565.0, y=575.0)
        print(f"Coordenadas de la Ciudad 1 (índice 0): {matriz_coord[0]}")
        print(f"Coordenadas de la Ciudad 2 (índice 1): {matriz_coord[1]}")
        
        # 2. Probar el cálculo de la matriz de distancias
        matriz_dist = calcular_matriz_distancia(matriz_coord, num_ciudades)
        print(f"\n[OK] Matriz de distancias calculada.")
        print(f"Dimensiones de la matriz de distancias: {matriz_dist.shape}")
        
        # Mostrar distancia entre la ciudad 0 y la ciudad 1
        dist_0_1 = matriz_dist[0][1]
        print(f"Distancia entre Ciudad 1 y Ciudad 2 : {dist_0_1:.2f}")
        
        print("=" * 55)
        print(" ¡TODO FUNCIONA CORRECTAMENTE!")
        print("=" * 55)
        
    except Exception as e:
        print(f"[ERROR] Hubo un problema al leer o procesar el archivo: {e}")