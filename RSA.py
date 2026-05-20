#Euclides Estendido
def euclides_estendido(a, b):
    # Caso base: evita divisão por zero
    if b == 0:
        print(f"mdc({a}, {b}) = {a}")
        print(f"{a} = {a} * 1 + {b} * 0")
        return a, 1, 0

    quociente = a // b
    resto = a % b

    print(f"{a} = {quociente} * {b} + {resto}")

    mdc, x1, y1 = euclides_estendido(b, resto)

    x = y1
    y = x1 - quociente * y1

    print(f"{a} * ({x}) + {b} * ({y}) = {mdc}")

    return mdc, x, y


def inverso_modular(d, phi):
    mdc, x, y = euclides_estendido(d, phi)

    if mdc != 1:
        print("Não existe inverso modular.")
        return None

    return x % phi

# codigo para criptografia RSA
# recebe a chave privada e retorna a publica

#queremos resolver 985e≡1(mod3444)
p = int(input())
q = int(input())
d = int(input())

# Sabendo que, no RSA, a chave pública é formada por (n, e), onde:
n = p*d
# e e é o inverso multiplicativo de d módulo φ(n)
phi = (p-1)*(q-1)

e = inverso_modular(d, phi)

print("n =", n)
print("phi =", phi)
print("e =", e)
print("Chave pública =", (n, e))

