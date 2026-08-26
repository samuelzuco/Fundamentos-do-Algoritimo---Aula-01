dias = int(input("digite a quantidade de dia: "))
horas = int(input("digite a quantidade de horas: "))
minutos = int(input("digite a quantidade de minutos: "))
segundos = int(input("digite a quantidade de segundos: "))

dia = 24*60*60*dias
hora = 60*60*horas
minuto = 60*minutos
segundo = segundos    

total_de_segundos = (dia + hora + minuto + segundo)

print("total de segundo", total_de_segundos)