valor_hora = float(input("digite o valor da hora:"))
horas_trabalhadas = float(input("digite a quantidade de horas trabalhadas:"))
salario = valor_hora * horas_trabalhadas

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

salario_liquido = salario - (ir + inss + sindicato)

print(f"Salario bruto: R$ {salario_liquido:.2f}")
print(f"ir (11%): R$ {ir:.2f}")
print(f"inss (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {inss:.2f}")
