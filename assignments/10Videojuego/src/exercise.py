def main():
    #escribe tu código abajo de esta línea
    new=input("Dame la cantidad de juegos nuevos: ")
used=input("Dame la cantidad de juegos usados: ")
total=(int(new)*1000)+(int(used)*350)
print("El total de la compra es: "+str(int(total)))
   pass



if __name__ == '__main__':
    main()
