from time import sleep
import currency_converter

currency_converter = currency_converter.CurrencyConverter()

print('\tCONVERSOR DE MOEDAS\n')

while True:
    quantidade = float(
        input("Qual a quantidade que deseja converter: \n"))
    print('-'*60)
    moeda_origem = int(input(
        'Escolha a moeda inicial \n [1] - USD \n [2] - BRL \n [3] - OUTRA \n'))
    print('-'*60)
    if moeda_origem == 1:
        moeda_origem = 'USD'
        print(f'Você escolheu a opção: {moeda_origem}')
        print('-'*60)
    elif moeda_origem == 2:
        moeda_origem = 'BRL'
        print(f'Você escolheu a opção {moeda_origem}')
        print('-'*60)
    elif moeda_origem == 3:
        moeda_origem = input(
            'Digite o código da moeda que deseja (3 digitos) ').upper()
        print(f'Você escolheu a opção: {moeda_origem}')
        print('-'*60)

    moeda_destino = int(input(
        'Escolha a moeda destino \n [1] - USD \n [2] - BRL \n [3] - OUTRA \n'))
    if moeda_destino == 1:
        moeda_destino = 'USD'  # moeda de destino
        print(f'Você escolheu a opção {moeda_destino}')
        print('-'*60)
    elif moeda_destino == 2:
        moeda_destino = 'BRL'
        print(f'Você escolheu a opção {moeda_destino}')
        print('-'*60)
    elif moeda_destino == 3:
        moeda_destino = input(
            'Digite o código da moeda que deseja (3 digitos) ').upper()
        print(f'Você escolheu a moeda: {moeda_destino}')

        print('-'*60)

    resultado = currency_converter.convert(
        quantidade, moeda_origem, moeda_destino)
    print('CONVERTENDO...')
    sleep(1.5)

    print(f'{quantidade} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino}')
    print('-'*60)
