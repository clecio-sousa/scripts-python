dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))

total_segundos = (dias *86400) + (horas * 3600) + (minutos * 60) + segundos

print("Total de segundos: {}".format(total_segundos))