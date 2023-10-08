import PySimpleGUI as sg


def transfer_data_window(items, get_drone_action, window1):
    # Layout
    
    transfer_data_layout = [
        [sg.Text("Transfer Data Screen")],
        [sg.Button("OK", size=(10,1)), sg.Button("Back", size=(10,1))],

        [sg.Input(key='-file_input-'),
            sg.Button('File Path')]
    ]    
        
    transfer_data_window = sg.Window("Transfer Data", transfer_data_layout, size=(
        1200, 800), element_justification='c', finalize=True)
    
    
    while True:
        event, values = transfer_data_window.read()
            
        if event in (sg.WIN_CLOSED, 'Back'):
            break
        if event == "OK":
            sg.popup("Button OK was clicked!")
            
    window1.un_hide()
    transfer_data_window.close()