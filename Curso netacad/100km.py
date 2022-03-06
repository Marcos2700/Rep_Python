#Transfromar de millas/galon a 100km/litros y viceversa
#1 milla = 1609.344 metros.
#1 galón = 3.785411784 litros
def l100kmtompg(liters):
    galon = liters/3.785411784
    millas = 100E3/1609.344
    return millas/galon

def mpgtol100km(miles):
    km100 = (miles*1609.344)/100E3
    return 3.785411784/km100



print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))