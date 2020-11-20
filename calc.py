from PySimpleGUI import PySimpleGUI as sg
import pyperclip

image_copy = './copy.png'
imposto = 5
tarifa_ml_classico = 12
tarifa_ml_premium = 17
tarifa_b2w = 16
tarifa_magalu = 20
tarifa_carrefour = 14
tarifa_via_varejo = 18

# Layout
sg.theme('Reddit')
frame_layout_dados = [
    [sg.Text('Preço de custo', size=(17,1)), sg.Input(key='custo', size=(10,1))],
    [sg.Text('Valor do frete', size=(17,1)), sg.Input(key='frete', size=(10,1))],
    [sg.Text('Margem de lucro %', size=(17,1)), sg.Input(key='margem', size=(10,1))],
    [sg.Button('Calcular', size=(26,1))]
]
frame_layout_copiar = [
    [sg.Button(image_filename=image_copy, key='copiar_meli_classico'),sg.Text('Mercado Livre (classico)')],
    [sg.Button(image_filename=image_copy, key='copiar_meli_premium'),sg.Text('Mercado Livre (premium)')],
    [sg.Button(image_filename=image_copy, key='copiar_b2w'),sg.Text('B2W')],
    [sg.Button(image_filename=image_copy, key='copiar_magalu'),sg.Text('Magalu')],
    [sg.Button(image_filename=image_copy, key='copiar_carrefour'),sg.Text('Carrefour')],
    [sg.Button(image_filename=image_copy, key='copiar_via_varejo'),sg.Text('Via Varejo')]
]
layout = [
    [sg.Frame(' Dados ',frame_layout_dados), sg.Frame(' Botão para copiar ',frame_layout_copiar)],
    [sg.Output(size=(58,10))]
]

# Janela
janela = sg.Window('Calculadora de preços para Marketplace', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    custo = float(valores['custo'])
    frete = float(valores['frete'])
    markup = float(valores['margem'])
    if eventos == sg.WINDOW_CLOSED:
        break

    # if eventos == 'Calcular':
    #     print(valores)
    #     print(valores['custo'])

    if eventos == 'Calcular':

        preco_bruto_meli_classico = custo / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
        if preco_bruto_meli_classico >= 99:
            preco_meli_maior_99_classico = (custo + frete) / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
            print(f'Mercado Livre Classico: R$ {preco_meli_maior_99_classico:.2f}')
        else:
            preco_meli_menor_99_classico = (custo + 5) / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
            print(f'Mercado Livre Classico: R$ {preco_meli_menor_99_classico:.2f}')

        preco_bruto_meli_premium = custo / (1 - imposto / 100 - markup / 100 - tarifa_ml_premium / 100)
        if preco_bruto_meli_premium >= 99:
            preco_meli_maior_99_premium = (custo + frete) / (1 - imposto / 100 - markup / 100 - tarifa_ml_premium / 100)
            print(f'Mercado Livre Premium: R$ {preco_meli_maior_99_premium:.2f}')
        else:
            preco_meli_menor_99_premium = (custo + 5) / (1 - imposto / 100 - markup / 100 - tarifa_ml_premium / 100)
            print(f'Mercado Livre Premium: R$ {preco_meli_menor_99_premium:.2f}')
        
        preco_b2w = custo / (1 - imposto / 100 - markup / 100 - tarifa_b2w / 100)
        print(f'B2w: R$ {preco_b2w:.2f}')

        preco_magalu = custo / (1 - imposto / 100 - markup / 100 - tarifa_magalu / 100)
        print(f'Magalu: R$ {preco_magalu:.2f}')

        preco_carrefour = custo / (1 - imposto / 100 - markup / 100 - tarifa_carrefour / 100)
        print(f'Careffour: R$ {preco_carrefour:.2f}')

        preco_via_varejo = custo / (1 - imposto / 100 - markup / 100 - tarifa_via_varejo / 100)
        print(f'Via Varejo: R$ {preco_via_varejo:.2f} \n \n \n')

    #if evento == 'Calcular':
        # preco_ml_classico = (custo + 5) / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
        # preco_ml_classico_com_frete = (custo + frete) / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
        # preco_ml_premium = 0

    if eventos == 'copiar_meli_classico':
        preco_bruto_meli_classico = custo / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
        if preco_bruto_meli_classico >= 99:
            preco_meli_maior_99_classico = (custo + frete) / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
            pyperclip.copy(round(preco_meli_maior_99_classico,2))
        else:
            preco_meli_menor_99_classico = (custo + 5) / (1 - imposto / 100 - markup / 100 - tarifa_ml_classico / 100)
            pyperclip.copy(round(preco_meli_menor_99_classico,2))
    if eventos == 'copiar_meli_premium':
        preco_bruto_meli_premium = custo / (1 - imposto / 100 - markup / 100 - tarifa_ml_premium / 100)
        if preco_bruto_meli_premium >= 99:
            preco_meli_maior_99_premium = (custo + frete) / (1 - imposto / 100 - markup / 100 - tarifa_ml_premium / 100)
            pyperclip.copy(round(preco_meli_maior_99_premium,2))
        else:
            preco_meli_menor_99_premium = (custo + 5) / (1 - imposto / 100 - markup / 100 - tarifa_ml_premium / 100)
            pyperclip.copy(round(preco_meli_menor_99_premium,2))
    if eventos == 'copiar_b2w':
        preco_b2w = custo / (1 - imposto / 100 - markup / 100 - tarifa_b2w / 100)
        pyperclip.copy(round(preco_b2w,2))
    if eventos == 'copiar_magalu':
        preco_magalu = custo / (1 - imposto / 100 - markup / 100 - tarifa_magalu / 100)
        pyperclip.copy(round(preco_magalu,2))
    if eventos == 'copiar_carrefour':
        preco_carrefour = custo / (1 - imposto / 100 - markup / 100 - tarifa_carrefour / 100)
        pyperclip.copy(round(preco_carrefour,2))
    if eventos == 'copiar_via_varejo':
        preco_via_varejo = custo / (1 - imposto / 100 - markup / 100 - tarifa_via_varejo / 100)
        pyperclip.copy(round(preco_via_varejo,2))

    