import PySimpleGUI as sg

layout = [[sg.Button(' ', key = str(row) + ' ' + str(col), size=(5,5)) for col in range(3)] for row in range(3)]

window = sg.Window('Window Title', layout)
lastupdate =  'o'


# def anyone_won():
#     return True  /False

# state_of_the_game = [
#     ['x', None, None],
#     [None, 'o', None],
#     [None, None, None]
# ]
# '0 0'.split(' ')
# ['0', '0']
# list(map(lambda x: int(x), ['0', '0']))
# [0, 0]

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    #if window[0 0], window[1 1], window[2 2] 
    state_of_the_game.append(event)
    print(state_of_the_game)
    # Output a message to the window
    
    if lastupdate == 'o':
        window[event].update('x')
        lastupdate =  'x'
    else:
        window[event].update('o')
        lastupdate =  'o'

    print(event)
    print(values)
# Finish up by removing from the screen
window.close()

# [
#     [sg.Button(f'{0}, {0}'), sg.Button(f'{0}, {1}'), sg.Button(f'{0}, {2}'), sg.Button(f'{0}, {3}')],
#     [sg.Button(f'{1}, {0}'), sg.Button(f'{1}, {1}'), sg.Button(f'{1}, {2}'), sg.Button(f'{1}, {3}')],
#     [sg.Button(f'{2}, {0}'), sg.Button(f'{2}, {1}'), sg.Button(f'{2}, {2}'),
# ]

