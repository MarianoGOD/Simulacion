import random

def lanzar_dados(cantidad):
    # Simula el lanzamiento de dados con distribución uniforme
    return [random.randint(1, 6) for _ in range(cantidad)]

def turno_jugador():
    # El jugador lanza 5 dados al principio
    dados = lanzar_dados(5)
    
    # Tiene hasta 2 intentos extra
    for _ in range(2):
        # Miro qué número salió más veces
        conteo = {x: dados.count(x) for x in set(dados)}
        mas_frecuente = max(conteo, key=conteo.get)
        
        # Guardo los dados repetidos y vuelvo a lanzar el resto
        dados_guardados = [mas_frecuente] * conteo[mas_frecuente]
        dados_a_lanzar = 5 - len(dados_guardados)
        
        if dados_a_lanzar == 0:
            break # Ya tengo 5 iguales, no necesito lanzar más
            
        dados = dados_guardados + lanzar_dados(dados_a_lanzar)
        
    # El puntaje es simplemente la suma de los dados al final
    return sum(dados)

def simulacion_montecarlo(n_partidas):
    v1 = 0
    v2 = 0
    empates = 0
    
    print(f"Iniciando simulación de {n_partidas} partidas de Yahtzee...")
    
    for _ in range(n_partidas):
        # 13 rondas por jugador
        puntaje_j1 = sum([turno_jugador() for _ in range(13)])
        puntaje_j2 = sum([turno_jugador() for _ in range(13)])
        
        if puntaje_j1 > puntaje_j2:
            v1 += 1
        elif puntaje_j2 > puntaje_j1:
            v2 += 1
        else:
            empates += 1
            
    print("--- RESULTADOS ---")
    print(f"Mariano ganó: {v1} veces")
    print(f"Estiven ganó: {v2} veces")
    print(f"Empataron: {empates} veces")

if __name__ == "__main__":
    simulacion_montecarlo(10000)
