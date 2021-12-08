qtde_cigarros = int(input("Quantidade de cigarros diarios:"))
anos_fumados = float(input("Anos fumados:"))

"""dias_fumados = anos_fumados * 365

dias_perdidos = qtde_cigarros * (0.007 * dias_fumados)

print(f"Dias perdidos:{dias_perdidos}")
"""
reducao_minutos = anos_fumados * 365 *qtde_cigarros*10
reducao_dias = reducao_minutos/(24*60)

print(f"Dias perdidos:{reducao_dias:.2f}")