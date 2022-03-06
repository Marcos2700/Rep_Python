def isYearLeap(year):
	if year < 0:
		return
	if year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 100 == 0 and year % 400 != 0:
		return False
	elif year % 400 == 0 and year % 100 == 0:
		return True
	else:
		return False

def daysInMonth(year, month):
	months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
	if months[month-1] == "enero" or months[month-1] == "marzo" or months[month-1] == "mayo" or months[month-1] == "julio" or months[month-1] == "agosto" or months[month-1] == "octubre" or months[month-1] == "diciembre":
		return 31
	elif months[month-1] == "abril" or months[month-1] == "junio" or months[month-1] == "septiembre" or months[month-1] == "noviembre":
		return 30
	elif months[month-1] == "febrero":
		if isYearLeap(year):
			return 29
		else:
			return 28

def dayOfYear(year, month, day):
    if day > daysInMonth(year, month):
        return

    logMonth = 1
    yearDay = 0

    while logMonth < month:
        yearDay += daysInMonth(year, logMonth)
        logMonth+=1
    yearDay+=day
    return yearDay

print(dayOfYear(2000, 2, 31))