# programa para calcular a multiplicação de matrizes em python
# no total temos as matrizes A de dimensao mn e B de dimensao pq
dimValidas = False

while not dimValidas:
    m = int(input("Insira quantidade de linhas da matriz A\n"))
    n = int(input("Insira quantidade de colunas da matriz A\n"))
              
    p = int(input("Insira quantidade de linhas da matriz B\n"))
    q = int(input("Insira quantidade de colunas da matriz B\n"))

    # n precisa ser igual a p para a multiplicacao ser possivel

    if (n == p):
        dimValidas = True

    else:
        print("dimensoes invalidas, insira novamente...\n")


A = [[0 for _ in range(n)] for _ in range(m)]
B = [[0 for _ in range(q)] for _ in range(p)]

for i in range(m):
    for j in range(n):
        A[i][j] = int(input(f"Insira o valor de a{i+1}{j+1}\n"))

print("matriz A criada: ")
for linha in A:
    print(linha)

for i in range(p):
    for j in range(q):
        B[i][j] = int(input(f"Insira o valor de b{i+1}{j+1}\n"))

print("\nmatriz B criada: ")
for linha in B:
    print(linha)

# uma nova matriz C sera criada que vai representar a multiplicacao

C = [[0 for _ in range(q)] for _ in range(m)]
print("c_ij = ∑ a_ik * b_kj com k variando de 1 a p\n")

# aqui eh aonde a logica comeca a aparecer
# na multiplicacao de matrizes, devemos multiplicar linha X coluna, sempre
soma = 0
for i in range(m):
    for j in range(q):
        for k in range(n): # aqui eh o limite p da soma
            print("index c_{i}{j} = {}")
            soma = soma + A[i][k] * B[k][j]
            C[i][j] = soma


print("\nmatriz multiplicacao de AB = C criada: ")
for linha in C:
    print(linha)
