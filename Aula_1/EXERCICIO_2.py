quilometros_percorridos = float(input("digite o KM percorrido:"))
dias = int(input("digite a quantidade de dia:"))
dia = 60.0 * dias
KM_percorridos = 0.15 * quilometros_percorridos

total_a_pagar = (dia + KM_percorridos)
print("total a pagar:", total_a_pagar)