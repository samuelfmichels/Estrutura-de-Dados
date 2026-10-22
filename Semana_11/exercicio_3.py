def caixas(topo, base=1):
    if topo < base:
        return
    print("Caixa:", topo)
    caixas(topo - 1, base)


def main():
    total_caixas = int(input("Digite o numero de caixas: "))
    caixas(total_caixas)


main()
