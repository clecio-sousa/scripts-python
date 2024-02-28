def tempo_total(total_minutos):
    horas = total_minutos / 60
    minutos = total_minutos % 60

    return print(f'Tempo total: {horas:.0f} horas e {minutos} minutos')


tempo_total(125)
