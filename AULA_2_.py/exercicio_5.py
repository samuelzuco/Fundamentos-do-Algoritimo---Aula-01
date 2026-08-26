ano_atual = int(input("digite o ano atual: "))
ano_nasc = int(input("digite seu ano de nascimento: "))

idade = ano_atual - ano_nasc

if idade >= 18:
    print("você pode tirar carta")

else:
    print("você não pode tirar carta")

