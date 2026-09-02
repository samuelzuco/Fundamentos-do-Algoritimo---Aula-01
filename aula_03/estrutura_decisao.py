preco=float(input("Digite o preço: "))
cod_origem=int(input("Digite o código do produto: "))

print(f"O seu produto tem o preço {preco} e o código {cod_origem}")

if cod_origem == 1:
    print("O seu produto tem origem o Sul")

elif cod_origem == 2:
    print("O seu produto tem origem o Norte")

elif cod_origem == 3:
    print("O seu produto tem origem o Leste")

elif cod_origem == 4:
    print("O seu produto tem origem o Oeste")    

elif cod_origem  >=5 and cod_origem <=6 or cod_origem >=25 and cod_origem <=30:
    print("O seu produto tem origem o Nordeste")

elif cod_origem  >=7 and cod_origem <=9:
    print("O seu produto tem origem o Sudeste")

elif cod_origem >=10 and cod_origem<=20:
    print("O seu produto tem origem o Centro-oeste")

else:
    print("O seu produto tem origem internacional")


