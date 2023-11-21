def monta_computador(cpu, hd, memoria, placa_video, monitor, **kwargs):
    print('O computador montado foi:')
    print(f'\tCPU: {cpu}')
    print(f'\tHD: {hd} TB')
    print(f'\tMemoria: {memoria}')
    print(f'\tPlaca de video: {placa_video}')
    print(f'\tMonitor: {monitor} polegadas')
    print(f'\tOutros perifericos: ')

    for chave, valor in kwargs.items():
        print(f'\t\t{chave}: {valor}')


monta_computador('core i9', 2, 32, 'RXT-150', monitor=17, webcam='Webcam multilaser', teclado='teclado multilase')
