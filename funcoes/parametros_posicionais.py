def funcao_com_args(arg1, arg2, *args):

    print(f'Arg1: {arg1}')
    print(f'Arg2: {arg2}')
    print(f'*Args: {args}')


funcao_com_args(1, 2, 3, 4, 5)