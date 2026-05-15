A = input("Insira um número: ") 
A = int(A)
B = input("Insira um número: ") 
B = int(B)
C = input("Insira um número: ") 
C = int(C)
D = input("Insira um número: ") 
D = int(D)
E = input("Insira um número: ") 
E = int(E)

Lista = [A, B, C, D]
Lista_nova = []
for item in Lista:
    multiplicacao = item * E
    Lista_nova.append(multiplicacao)
print(Lista_nova)