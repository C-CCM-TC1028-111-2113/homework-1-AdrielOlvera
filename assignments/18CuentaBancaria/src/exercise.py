def main():
    #escribe tu código abajo de esta línea
    saldo=input("Dame el saldo del mes anterior: ")
ing=input("Dame los ingresos: ")
egr=input("Dame los egresos: ")
cheq=input("Dame el número de cheques: ")
final=(float(saldo)+float(ing)-float(egr)-(int(cheq)*13))
perc=((float(final)*7.5)/100)
total=float(final)-float(perc)
print("El saldo final de la cuenta es: "+str(total))

    pass

if __name__ == '__main__':
    main()
