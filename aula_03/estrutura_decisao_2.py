A = int(input("Digite um número: "))
B = int(input("Digite um outro número diferente: "))
C = int(input("Digite mais um número diferente: "))

if A > B > C:
    print(f"{A} > {B} > {C}")
elif A > C >B:
    print(f"{A} > {C} > {B}")
elif B > A > C:
    print(f"{B} > {A} > {C}")
elif B > C >A:
    print(f"{B} > {C} > {A}")
elif C > B > A:
    print(f"{C} > {B} > {A}")
else:
    print(f"{C} > {A} > {B}")




