import PySimpleGUI as sg
import numpy as np  

layout = [[sg.Button(' ', key = str(row) + ' ' + str(col), size=(5,5)) for col in range(3)] for row in range(3)]

window = sg.Window('Window Title', layout)
lastupdate =  'o'

def check_rows_and_cols(row_or_columns):
    for row_or_column in row_or_columns:
        if all(row_or_column) and row_or_column[0]:
            return True

def anyone_won(state_of_the_game):   
    diagonal1 = [state_of_the_game[0][0], state_of_the_game[1][1], state_of_the_game[2][2]]
    diagonal2 = [state_of_the_game[2][0], state_of_the_game[1][1], state_of_the_game[0][2]]
    diagonals = [diagonal1, diagonal2]

    if check_rows_and_cols(state_of_the_game) or check_rows_and_cols(np.transpose(state_of_the_game)) or check_rows_and_cols(diagonals): return True
    return False   


state_of_the_game = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    x = int(event[2])
    y = int(event[0])    

    if lastupdate == 'o':
        window[event].update('x')
        lastupdate =  'x'
        state_of_the_game[y][x] = 'x'
    else:
        window[event].update('o')
        lastupdate =  'o'
        state_of_the_game[y][x] = 'o'

    if anyone_won(state_of_the_game):
        break
window.close()
