import datetime
#Determinar signo zodiacal
def Signo(d, m):
    signo = ['acuario','piscis','aries','tauro','geminis','cancer','leo','virgo','libra','escorpio','sagitario','capricornio']
    if((d >= 20) and (m == 1) or (d < 19) and (m == 2)):
        return signo[0]
    elif((d >= 19) and (m == 2) or (d < 21) and (m == 3)):
        return signo[1]
    elif((d >= 21) and (m == 3) or (d < 20) and (m == 4)):
        return signo[2]
    elif((d >= 20) and (m == 4) or (d < 21) and (m == 5)):
        return signo[3]
    elif((d >= 21) and (m == 5) or (d < 21) and (m == 6)):
        return signo[4]
    elif((d >= 21) and (m == 6) or (d < 23) and (m == 7)):
        return signo[5]
    elif((d >= 23) and (m == 7) or (d < 23) and (m == 8)):
        return signo[6]
    elif((d >= 23) and (m == 8) or (d < 23) and (m == 9)):
        return signo[7]
    elif((d >= 23) and (m == 9) or (d < 23) and (m == 10)):
        return signo[8]
    elif((d >= 23) and (m == 10) or (d < 22) and (m == 11)):
        return signo[9]
    elif((d >= 22) and (m == 10) or (d < 22) and (m == 12)):
        return signo[10]
    else:
        return signo[11]
#Solicitar la fecha
print('Por favor, indique su fecha de nacimiento')
dia = int(input('Indique el dia de nacimiento ---> '))
mes = int(input('Indique el numero del mes en que nacio ---> '))
año = int(input('Indique el año en que nacio ---> '))
#Declarar la fecha
date = datetime.datetime(año, mes, dia)
now = datetime.datetime.now()
#Encontrar el tiempo de vida
time = now - date
#Encontrar el tiempo vivido
days = time.days
print("")
print('Dias vividos: ', days)
seconds = time.seconds + ((days*24)*3600)
hours = seconds / 3600
print('Horas vividas:', hours)
print('Segundos vividos: ', seconds)
zodiaco = Signo(dia, mes)
print('Signo zodiacal: ', zodiaco)




