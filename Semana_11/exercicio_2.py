def media_temperaturas(vetor, indice=0):
    if indice == len(vetor):
        return 0
    soma = vetor[indice] + media_temperaturas(vetor, indice + 1)
    if indice == 0:
        return soma / len(vetor)
    return soma


def main():
    temperaturas = [18, 22, 25, 30, 20]
    media = media_temperaturas(temperaturas)
    print("Media das temperaturas:", media)


main()
