ano_carro = int(input("digite o ano do seu carro: "))
ano_atual = int(input("digite o ano atual: "))

idade_carro = ano_atual - ano_carro

if idade_carro < 3:
    print("seu carro é novo")

else: 
    print("seu carro é véio")


