import json
#cantidad de palabras repetidas
def Repetidas(file):
    usadas = []
    cantidad = 0
    for x in file:
        if(not x in usadas):
            usadas.append(x)
            xCont = file.count(x)
            if(xCont > 1):
                cantidad += 1
    return cantidad
#cantidad de palabras que solo contienen numeros
def Numeros(file):
    cantidad = 0
    for x in file:
        if(type(x) == int or type(x) == float ):
            cantidad += 1
    return cantidad
#cantidad de palabras que solo contienen letras
def Palabras(file):
    cantidad = 0
    for x in file:
        if(type(x) == str):
            cantidad += 1
    return cantidad

file = 'laboratorio_2_1.json'
with open(file) as content:
    result = json.load(content)
    rep = Repetidas(result)
    nums = Numeros(result)
    palbs = Palabras(result)
    print('La cantidad de palabras repetidas es de : ', rep)
    print('La cantidad de palabras que solo contienen numeros es de: ', nums)
    print('La cantidad de palabras que solo contienen letras es de: ', palbs)
    
    