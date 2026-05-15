V1 = input("insira um número: ")
V2 = input("insira um número: ")

if not V1 or not V2:
    A = None
    print("Erro, não digitou algum valor!")

if V1 == V2:
    A = True
    print("valores iguais!")

else:
    A = False
    print("Valores diferentes!!!")

