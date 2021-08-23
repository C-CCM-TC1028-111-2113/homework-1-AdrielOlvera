def main():
    #escribe tu código abajo de esta línea
    msj=input("Dame el número de mensajes: ")
mgs=input("Dame el número de megas: ")
mins=input("Dame el número de minutos: ")
costo=(int(msj)+float(mgs)+int(mins))*0.8
print("El costo mensual es: "+str(float(costo)))

    #Leer los datos
    pass


if __name__ == '__main__':
    main()
