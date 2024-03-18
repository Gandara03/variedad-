def grabar_rango_de_alturas():
    disciplina="-"
    altura="0.1"
    try:
        archivo_atletas=open("atletas.txt","wt")
        disciplina=input("ingrese la disciplina del atleta o enter para finalizar: ")
        while disciplina!="":
            Numero_de_atleta=0
            archivo_atletas.write(disciplina+":"+'\n')
            altura = input("ingrese la altura del atleta o Enter para terminar :")
            while altura!="":
                Numero_de_atleta=int(Numero_de_atleta)
                Numero_de_atleta=Numero_de_atleta+1
                Numero_de_atleta=str(Numero_de_atleta)
                if altura!="":
                    archivo_atletas.write("  altura del atleta "+Numero_de_atleta+": "+altura+'\n')
                altura = input("ingrese la altura del atleta o Enter para terminar :")
            disciplina=input("ingrese la disciplina del atleta o enter para finalizar:")
        print("Archivo creado correctamente.")
    except FileNotFoundError as mensaje:
        print ("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede grabar el archivo:",mensaje)
    finally:
        try:
            archivo_atletas.close()
        except NameError:
            pass
    
def Grabar_promedio():
    try:
        contador=0
        acumulador=0
        archivo_promedios=open("promedios.txt","wt")
        archivo_atletas=open("atletas.txt","rt")
        for linea in archivo_atletas:
            if len(linea) >20:
                linea = linea.strip('\n')
                linea=linea[::-1]
                altura= linea[0:4]
                altura=altura[::-1]
                acumulador=acumulador+float(altura)
                contador=contador+1
                promedio=str(acumulador/contador)
                promedio=promedio[0:4]
            else:
                if contador >0:
                    archivo_promedios.write("  Altura promedio del deporte:"+promedio+'\n')
                deporte=linea
                archivo_promedios.write(deporte)
                contador=0
                acumulador=0
        archivo_promedios.write("  Altura promedio del deporte:"+promedio+'\n')   
    except FileNotFoundError as mensaje:
        print ("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            archivo_atletas.close()
            archivo_promedios.close()
        except NameError:
            pass
    
def MostrarMasAltos():
    archivo_promedios=open("promedios.txt","rt")
    superior=0
    try:
        contador=0
        acumulador=0
        for linea in archivo_promedios:
            if len(linea) >20:
                linea = linea.strip('\n')
                altura= linea[30:35]
                acumulador=acumulador+float(altura)
                contador=contador+1
                promediodepromedio=acumulador/contador
        archivo_promedios.seek(0)
        print("promedio de las alturas de los deportistas:",promediodepromedio)
        print("---------------------------------------")
        print("deportes con estatura mas alta que la promedio:")
        for linea in archivo_promedios:
            if len(linea) <20:
                deporte=linea
            else:
                linea = linea.strip('\n')
                promedio= linea[30:35]
                promedio=float(promedio)
                if promedio>promediodepromedio:
                    superior=promediodepromedio-promedio
                    print(deporte,"es superior al promedio de estaturas generales por :",superior)
    except FileNotFoundError as mensaje:
        print ("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            archivo_promedios.close()
        except NameError:
            pass

#programa principal    
grabar_rango_de_alturas()
Grabar_promedio()
MostrarMasAltos()