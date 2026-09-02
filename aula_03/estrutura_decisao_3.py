genero = str(input("Digite seu genero: "))
altura = float(input("Digite sua altura em metros: "))

formula_homem = (72.7 * altura) - 58
formula_mulher = (62.1 * altura) - 44.7

if genero =="homem":
    print(f"Seu peso ideal é: {formula_homem}")
else:
    print(f"Seu peso ideal é: {formula_mulher}")

    


