def calcula_media_mediana(notas):
    media = sum(notas) / len(notas)
    mediana = 0

    if len(notas) % 2 == 0:
        indice_ponto_central_menor = int(len(notas)/2 - 1)
        indice_ponto_central_maior = int(len(notas)/2)
        ponto_central_maior = notas[indice_ponto_central_maior]
        ponto_central_menor = notas[indice_ponto_central_menor]
        mediana = (ponto_central_maior + ponto_central_menor) / 2
        #  numero par de elementos
        pass

    else:
        notas_ordenadas = sorted(notas)  # Ordem crescente de numeros
        indice_mediana = int(len(notas) / 2)
        mediana = notas_ordenadas[indice_mediana]
        # numero impar de elementos 6 7 8 10

    return media, mediana


resultado_media, resultado_mediana = calcula_media_mediana([6, 7, 8, 10])
print(resultado_media)
print(resultado_mediana)
