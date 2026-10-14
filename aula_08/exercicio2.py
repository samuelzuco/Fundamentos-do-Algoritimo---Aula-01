L = []

for i in range(10):
    x = int(input())
    L.append(x)

maior = L[0]
indMaior = 0
for i in range(len(L)):
    if L[i] > maior:
        maior = L[i]
        indMaior = i
print("O maior valor da lista é:", maior)
print("O índice do maior valor é:", indMaior)
