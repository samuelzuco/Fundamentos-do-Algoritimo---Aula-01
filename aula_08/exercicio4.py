L = []
soma = 0

for i in range(10):
    x = int(input("Digite um número: "))
    L.append(x)
    if L[i] % 2 == 0:
        soma += L[i]
    elif L[i] % 2 != 0:
        soma += 0

print("A soma dos números pares da lista é:", soma)
print("A soma dos números ímpares da lista é:", sum(L) - soma)



