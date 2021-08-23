def main():
    #escribe tu código abajo de esta línea
    import math
words=input("Dame el número de palabras: ")
pages=math.ceil(int(words)/475)
cost=int(pages)*60
discount=(int(cost)*10)/100
total=int(cost)-float(discount)
print("El costo de la publicación es: "+str(total))

    pass


if __name__ == '__main__':
    main()
