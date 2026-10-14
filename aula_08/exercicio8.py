L = []

while True:
    palavra = input("Digite uma palavra: ")
    if palavra == "":
        break
    
    if not palavra in L:
        L.append(palavra)

print("Palavras digitadas: ")
for palavra in L:
    print(palavra)