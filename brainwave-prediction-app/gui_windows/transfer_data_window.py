import PySimpleGUI as sg
import sys
import os

def transfer_data_window(window1):

    def is_valid_directory(input_value):
        # Check if the input is a valid directory path
        return os.path.isdir(input_value)
    
    # Positions items in top left corner of the window
    top_left = [
        [sg.Button('Home', size=(8, 2), image_filename="../brainwave-prediction-app/images/home.png")]     
    ]

    # Positions items in the top center of the window
    title_font_size = 35   # adjust title font size
    top_center = [
        [sg.Text("Transfer Data Screen", font=('Arial', title_font_size), justification='c', auto_size_text=True)]    
    ]

    # Contains items for directory input of user in the window
    directory_input_message_size = 13   # adjut directoy input message size
    directory_input = [
        [sg.Text("Select a locally stored directory for transfer...", font=('Arial', directory_input_message_size))],
        [sg.Text('Folder Path:'), sg.Input(key='-dir_input-'), sg.FolderBrowse(target='-dir_input-')],
    ]

    # Combined window layout
    transfer_data_layout = [
        [sg.Column(top_left), sg.Push(), sg.Column(top_center, pad=((0, 175), 0)), sg.Push(), ],
        [sg.Column(directory_input, pad=(0, (125, 25)))],
        [sg.Button("Transfer", size=(10,1))]    # Button for executing transfer       
    ]    
    
    # Window
    transfer_data_window = sg.Window("Transfer Data", transfer_data_layout, size=(
        1200, 800), element_justification='c', finalize=True, grab_anywhere=True) 

    # Event loop    
    while True:
        event, values = transfer_data_window.read()
            
        if event == sg.WIN_CLOSED:    # completely close program if 'x' is clicked
            sys.exit()
        elif event == "Home":   # return to start screen
            break
        elif event == "Transfer":   # check if valid directory and transfer
            selected_directory = values['-dir_input-']
            if is_valid_directory(selected_directory):
                sg.popup(f"Selected folder: {selected_directory}")
            else:
                sg.popup("Invalid directory. Please select a valid directory.")
                transfer_data_window['-dir_input-'].update('')

    window1.un_hide()
    transfer_data_window.close()

