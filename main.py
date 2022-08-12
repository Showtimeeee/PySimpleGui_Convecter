import PySimpleGUI as sg


# enable_events=True включает собыите с кнопки
maket = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['км в мили', 'кг в фунты'], key='-UNITS-'),
        sg.Button('START', key='-CONVERT-')
    ],
    [sg.Text('Введите число', key='-OUTPUT-')]
]
window = sg.Window('Конвектер', maket)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'км в мили':
                    output = (float(input_value) * 0.6214,2)
                    output_string = f'{input_value} в км {output} миль.'
                case 'кг в фунты':
                    output = (float(input_value) * 2.20462,2)
                    output_string = f'{input_value} в кг {output} фунтов.'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Введите занчение')



window.close()
