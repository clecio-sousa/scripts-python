km_percorrido = float(input("Quilometros percorridos:"))
dias_alugados = int(input("Dias alugados:"))


preco_total = (km_percorrido * 0.15) + (dias_alugados * 60.0)

print("Preço total: {}".format(preco_total))
