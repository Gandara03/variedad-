def imprimir_matriz_recursividad(matriz,fila,columna=0): # -RECURSIVIDAD-
    if fila<len(matriz):
        for columna in range(len(matriz[fila])):
            print(matriz[fila][columna],end="")
        print("")
        imprimir_matriz_recursividad(matriz,fila+1)
    else:
        print("\n")
def puntaje_y_registro_en_archivo(nombre_jugador, intentos,jugadores):
    salida=open("lista_de_puntos.txt","a")
    total_puntos=12
    if intentos==6:
        puntaje=total_puntos+3
    else:
        puntaje=intentos*2
    print("El jugador",nombre_jugador, "sumo:",puntaje,"puntos\n")
    try:
            a=str(nombre_jugador)+";"+str(puntaje)+"\n"
            salida.write(a)
    except FileNotFoundError as mensaje:
            print("No se pudo abrir el archivo", mensaje)
    except OSError as mensaje:
            print("ERROR", mensaje)
    else:
        pass
    finally:
        try:
            salida.close()
        except NameError:
            pass
        
def leerarchivo():       
try:
        lista_puntos=open("lista_de_puntos.txt","rt")
        for linea in lista_puntos:
                linea=linea.strip('\n')
                linea=linea.split(";")
                linea[1]=int(linea[1])
                if linea[1] > mayor_puntaje[1]:
                    mayor_puntaje[0]=linea[0]
                    mayor_puntaje[1]=linea[1]
                    jugadoresempatados=[]
                elif linea[1]==mayor_puntaje[1]:
                    if len(jugadoresempatados)==0:
                        jugadoresempatados=[mayor_puntaje[0],linea[0]]
                    else:
                        jugadoresempatados.append(linea[0])
    finally:
        try:
            lista_puntos.close()
        except NameError:
                pass
