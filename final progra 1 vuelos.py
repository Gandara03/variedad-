def crearmatriz(filas=8,columnas=4):
    matriz=[['D']*columnas for i in range (filas)]
    return matriz

def mostraravion(matriz, asientos):
    fila=1
    asientos=['V','X','Y','Z']
    print('		{0}	{1}	{2}	{3}'.format(asientos[0],asientos[1],asientos[2],asientos[3]))
    print()
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        print(f'FILA {fila}	', end="")
        for c in range(columnas):
            print('	{:4s}'.format(matriz[f][c]), end =" ")
        fila=fila+1
        print()
    print()
    
def validavuelo():
    while True:
        vuelo=int(input('Ingrese un numero de vuelo de 4 digitos: '))
        if 999<vuelo<10000 or vuelo==-1:
            break
        else:
            print('ingrese un vuelo valido')
    return vuelo

def validafila():
    while True:
        fila=int(input('Ingrese un numero de fila del 1 al 8: '))
        if 0<fila<9:
            break
        else:
            print('ingrese una fila valida')
    return fila

def validaasientos(asientos):
    while True:
        asiento=input('Ingrese un numero de asiento entre V,X,Y,X: ')
        asiento=asiento.upper()
        if asiento in asientos:
            break
        else:
            print('ingrese un asiento valido')
    return asiento

def generaroferta(asientos):
    try:
        oferta=open(r'T:\PINELLI BERNARD MILTON IGNACIO\oferta.txt','wt')
    except IOError:
        print('No se encontro el archivo')
    else:
        try:
            vuelo=validavuelo()
            importe=int(input('INGRESE EL PRECIO DEL ASIENTO DE ESTE VUELO: '))
            oferta.write(str(vuelo)+';'+str(importe)+'\n')
        except ValueError :
            print('valor ingresado erroneo')
        finally:
            oferta.close()

def generarventas(asientos):
    try:
        venta=open(r'T:\PINELLI BERNARD MILTON IGNACIO\ventas.txt','wt')
    except IOError:
        print('No se encontro el archivo')
    else:
        try:
            while True:
                vuelo=validavuelo()
                if vuelo ==-1:
                    break 
                fila=validafila()
                asiento=validaasientos(asientos)
                venta.write(str(vuelo)+';'+str(fila)+';'+asiento+'\n')
                
        except ValueError :
            print('valor ingresado erroneo')
        finally:
            venta.close()
            
def verificardisponibilidad(avion, asientos):
    try:
        oferta=open(r'T:\PINELLI BERNARD MILTON IGNACIO\oferta.txt','rt')
    except IOError:
        print('No se encontro el archivo')
    else:
        linea=oferta.readline()
        vuelo,precio=linea.strip('\n').split(';')
        vuelo=int(vuelo)
        precio=int(precio)
        
    try:
        ventas=open(r'T:\PINELLI BERNARD MILTON IGNACIO\ventas.txt','rt')
    except IOError:
        print('No se encontro el archivo')
    else:
        
        linea=ventas.readline()
        while linea:
            vuelov,fila,asiento=linea.strip('\n').split(';')
            vuelov=int(vuelo)
            fila=int(fila)
            if vuelov==vuelo:
                if avion[fila-1][asientos.index(asiento)]=="D":
                    avion[fila-1][asientos.index(asiento)]='R'
                else :
                    print('SE DETECTARON RESERVAS NO DISPONIBLES')
                    print()
            linea=ventas.readline()
            
    finally:
        print()
        cad='VENTAS DEL VUELO NRO '+str(vuelo)
        print(cad.center(40,"*"))
        print("*"*40)
        oferta.close()
        ventas.close()
    return precio
        
def informe(avion):
    filas = len(avion)
    columnas = len(avion[0])
    disponibles=0
    ocupadas=0
    for f in range(filas):
        for c in range(columnas):
            if avion[f][c]=='D':
                disponibles=disponibles+1
            if avion[f][c]=='R':
                ocupadas=ocupadas+1
    return disponibles, ocupadas
    
asientos=['V','X','Y','Z']            
avion=crearmatriz()
mostraravion(avion, asientos)
generaroferta(asientos)
generarventas(asientos)
while True:
    iniciar=input('DESEA OFERTAR EL VUELO - S=SI O N=NO -: ')
    iniciar=iniciar.upper()
    if iniciar=='S':
        print()
        print('INICIANDO')
        print()
        verificardisponibilidad(avion, asientos)
        break
    elif iniciar=='N':
        print('OFERTA DECLINADA - CERRANDO')
        break
    else:
        iniciar=input('DESEA OFERTAR EL VUELO - S=SI O N=NO -: ')
print()
mostraravion(avion, asientos)  
disponibles,ocupadas= informe(avion)
try:
    oferta=open(r'T:\PINELLI BERNARD MILTON IGNACIO\oferta.txt','rt')
except IOError:
    print('No se encontro el archivo')
else:
    linea=oferta.readline()
    vuelo,precio=linea.strip('\n').split(';')
    precio=int(precio)
    print(f'EL TOTAL FACTURADO DEL VUELO FUE DE ${precio*ocupadas}.-')
finally:
    oferta.close()
print()
print(f'QUEDAN UN TOTAL DE ASIENTOS SIN RESERVA DE {disponibles}')