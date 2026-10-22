def contagem_regressiva(n):
    if n == 1:
        print(1)
        return
    print(n)
    contagem_regressiva(n - 1)


def pares(n, atual=0):
    if atual > n:
        return
    print(atual)
    pares(n, atual + 2)


def soma_impares(n):
    if n <= 0:
        return 0
    if n % 2 != 0:
        return n + soma_impares(n - 2)
    return soma_impares(n - 1)


def main():
    contagem_regressiva(5)

    n_par = int(input("Digite um numero: "))
    pares(n_par)

    n_impar = int(input("Digite um numero: "))
    resultado = soma_impares(n_impar)
    print("Soma dos impares:", resultado)


main()
