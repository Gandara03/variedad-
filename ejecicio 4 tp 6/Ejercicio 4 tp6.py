def dividirpaises():
    archivo_nombres=open("C:/Users/alexi/Desktop/ejecicio 4 tp 6","r")
    archivo_armenia=open("ARMENIA.TXT","wr")
    archivo_italia=open("ITALIA.TXT","wr")
    archivo_españa=open("ESPAÑA.TXT","wr")
    try:
        for linea in archivo_nombres:
            linea[::1]
            if linea[0:3] =="ian":
                print("a")

    except FileNotFoundError as mensaje:
        print ("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            archivo_promedios.close()
        except NameError:
            pass
dividirpaises()