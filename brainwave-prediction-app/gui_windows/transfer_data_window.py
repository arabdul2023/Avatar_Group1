import PySimpleGUI as sg
import sys
import os

def transfer_data_window(items, get_drone_action, window1):


    def is_valid_directory(input_value):
        # Check if the input is a valid directory path
        return os.path.isdir(input_value)
    
    # Layout
    header_font_size = 35
    data_transfer_message_size = 13
    top_left = [
        [sg.Button('Home', size=(8, 2), image_filename="../brainwave-prediction-app/images/home.png")]     
    ]
    
    top_center = [
        [sg.Text("Transfer Data Screen", font=('Arial', header_font_size), justification='c', auto_size_text=True)]    
    ]
    
    data_transfer = [
        [sg.Text("Select a locally stored directory for transfer...", font=('Arial', data_transfer_message_size))],
        [sg.Text('Folder Path:'), sg.Input(key='-dir_input-'), sg.FolderBrowse(target='-dir_input-')],
    ]

    transfer_data_layout = [
        [sg.Column(top_left), sg.Push(), sg.Column(top_center, pad=((0, 175), 0)), sg.Push(), ],
        [sg.Column(data_transfer, pad=(0, (125, 25)))],
        [sg.Button("Transfer", size=(10,1))]        
    ]    
        
    transfer_data_window = sg.Window("Transfer Data", transfer_data_layout, size=(
        1200, 800), element_justification='c', finalize=True) 
    
    while True:
        event, values = transfer_data_window.read()
            
        if event == sg.WIN_CLOSED:
            sys.exit()
        elif event == "Home":
            break
        elif event == "Transfer":
            #sg.popup("Button OK was clicked!")
            selected_directory = values['-dir_input-']
            if is_valid_directory(selected_directory):
                sg.popup(f"Selected folder: {selected_directory}")
            else:
                sg.popup("Invalid directory. Please select a valid directory.")
                # Clear the invalid input
                transfer_data_window['-dir_input-'].update('')
 
    window1.un_hide()
    transfer_data_window.close()