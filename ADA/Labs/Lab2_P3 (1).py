#imprimir estrellas
def Estrellas(n):
    line = 0
    estr = '*'
    while(n > line):
        outp = ''
        x = line + 1
        while(x > 0):
            outp = outp + estr
            x = x - 1
        print(outp)
        line = line +1
print('Impresion de estrellas segun un numero ingresado')
cant = int(input("Ingrese un numero: "))
Estrellas(cant)