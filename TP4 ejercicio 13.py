#ejercicio 3

#funciones
#funcion para realizar cambio de numero a letra
def cambiodenumaletra(numeroingresado,listafinal,largodenumero):
    listafinal=[]
    listatransitoria=[]
    contador1=0
    contador2=0
    contador3=0
    contador4=0
    contador5=0
    #listas para cambiar de numero a letra
    lista1a20a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    lista1a20b=["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve","veinte","veintiuno","ventidos","ventitres","venticuatro","venticinco","ventiseis","ventisiete","ventiocho","ventinueve"]
    lista20a90a=[30,40,50,60,70,80,90]
    lista20a90b=["treinta y","cuarenta y","cincuenta y","sesenta y","setenta y","ochenta y","noventa y"]
    lista100a900a=[100,200,300,400,500,600,700,800,900]
    lista100a900b=["ciento" ,"docientos" ,"trecientos" ,"cuatrocientos" ,"quinientos" ,"seisientos" ,"setecientos" ,"ochocientos" ,"novecientos" ]
    listacantidad=cantidaddenumeros(numeroingresado,largodenumero)
    print(listacantidad)
    #cambio de numero a letra
    for i in range(len(listacantidad)):
        numeroingresado=int(listacantidad[i])
        if numeroingresado>=100 and numeroingresado <=999 :
            contador1=0
            cien=False
            while (numeroingresado -contador1)/100!=numeroingresado//100:
                contador1=contador1+1
            if numeroingresado==100:
                cien=True
            numeroingresado=numeroingresado-contador1
            contador2=lista100a900a.count(numeroingresado)
            if contador2 !=0 :
                contador2=lista100a900a.index(numeroingresado)
                if cien:
                    listatransitoria.append("cien")
                else:
                    listatransitoria.append(lista100a900b[contador2])
                numeroingresado=contador1
        if numeroingresado>=30 and numeroingresado <100 :
            contador3=0
            while (numeroingresado -contador3)/10!=numeroingresado//10 and numeroingresado/10!=numeroingresado//10 :
                contador3=contador3+1
            if numeroingresado/10!=numeroingresado//10:
                numeroingresado=numeroingresado-contador3
            contador4=lista20a90a.count(numeroingresado)
            if contador4 !=0 :
                contador4=lista20a90a.index(numeroingresado)
                variableparacolocarY=lista20a90b[contador4]
                numeroingresado=contador3
                if contador3==0:
                    numeroingresado=variableparacolocarY.replace("y","")
                    listatransitoria.append(variableparacolocarY)
                else:
                    listatransitoria.append(variableparacolocarY)
        if numeroingresado<30 and numeroingresado >0:
            contador5=lista1a20a.count(numeroingresado)
            if contador5 !=0 :
                contador5=lista1a20a.index(numeroingresado)
                numeroingresado=lista1a20b[contador5]
                listatransitoria.append(lista1a20b[contador5])
        cad=" ".join(listatransitoria)
        listatransitoria.clear()
        listafinal.append(cad)
#coloca los billones,millones,miles,etc
    if largodenumero ==10:
        listafinal[0]="Un billon"
    elif largodenumero<=9 and largodenumero>6:
        if listafinal[0]=="uno":
            listafinal[0]=listafinal[0].replace("uno","un")
            listafinal.insert(1,"millon")
        else:
            listafinal.insert(1,"millones")
            listafinal[0]=listafinal[0].replace("uno","un")
        if listafinal[2]=="uno":
            listafinal[2]="mil"
        else:
            listafinal.insert(3,"mil")
            listafinal[2]=listafinal[2].replace("uno","un")
    elif largodenumero<=6 and largodenumero>=4:
        if listafinal[0]=="uno":
            listafinal[0]="mil"
        else:
            listafinal.insert(1,"mil")
            listafinal[0]=listafinal[0].replace("uno","un")
    return listafinal
#funcion para obtener string y largo del numero ,con el objetivo de detectar miles,millones,billones,etc
def cantidaddenumeros(numeroingresado,largodenumero):
    listadestring=[]
    numeroingresado=str(numeroingresado)
    if largodenumero==10:
        listadestring.append(numeroingresado[0])
        listadestring.append(numeroingresado[1:4])
        listadestring.append(numeroingresado[4:7])
        listadestring.append(numeroingresado[7:10])
    elif largodenumero==9:
        listadestring.append(numeroingresado[0:3])
        listadestring.append(numeroingresado[3:6])
        listadestring.append(numeroingresado[6:9])
    elif largodenumero==8:
        listadestring.append(numeroingresado[0:2])
        listadestring.append(numeroingresado[2:5])
        listadestring.append(numeroingresado[5:8])
    elif largodenumero==7:
        listadestring.append(numeroingresado[0])
        listadestring.append(numeroingresado[1:4])
        listadestring.append(numeroingresado[4:7])
    elif largodenumero==6:
        listadestring.append(numeroingresado[0:3])
        listadestring.append(numeroingresado[3:6])
    elif largodenumero==5:
        listadestring.append(numeroingresado[0:2])
        listadestring.append(numeroingresado[2:5])
    elif largodenumero==4:
        listadestring.append(numeroingresado[0])
        listadestring.append(numeroingresado[1:4])
    else :
        listadestring.append(numeroingresado)
    return listadestring
#programa principal
listafinal=[]
numeroingresado=int(input("ingrese el numero:"))
while numeroingresado >= 1000000001:
    numeroingresado=int(input("ingrese el numero nuevamente (menor o igual a un billon):"))
if numeroingresado >0:
    largodelnumero=len(str(numeroingresado))
    listafinal=cambiodenumaletra(numeroingresado,listafinal,largodelnumero)
    numeroconletras=" ".join(listafinal)
    print(numeroconletras)
elif numeroingresado<0 and numeroingresado >=-1000000000:
    numeroingresado=str(numeroingresado)
    numeroingresado=numeroingresado.replace("-","")
    largodelnumero=len(str(numeroingresado))
    listafinal=cambiodenumaletra(numeroingresado,listafinal,largodelnumero)
    listafinal.insert(0,"menos")
    numeroconletras=" ".join(listafinal)
    print(numeroconletras)
else:
    print("el numero ingresado es cero")