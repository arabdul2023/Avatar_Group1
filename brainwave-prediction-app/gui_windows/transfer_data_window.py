import PySimpleGUI as sg
import sys
import os

def transfer_data_window(window1):

    file_path = "../file-transfer/sftp.py"
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            #sg.popup(f'File Contents:\n{file_contents}' )

    def is_valid_directory(input_value):
        # Check if the input is a valid directory path
        return os.path.isdir(input_value)
    
    # Positions items in top left corner of the window
    top_left = [
    #    [sg.Button('Home', size=(8, 2), image_filename="../brainwave-prediction-app/images/home.png")]     
    ]

    # Positions items in the top center of the window
    title_font_size = 35   # adjust title font size
    header = [
        [sg.Text("Transfer Data Screen", font=('Arial', title_font_size), justification='c', pad=((0,0),(100,50)), auto_size_text=True)]    
    ]

    login_data = [
        [sg.Text('Host:\t   '), sg.Input('', key='-host_input-')],
        [sg.Text('User Name:'), sg.Input('', key='-name_input-')],
        [sg.Text('Private Key:'), sg.Input('', key='-key_input-', password_char='*')],
        [sg.Text('Password:  '), sg.Input('', key='-pass_input-', password_char='*')],
        [sg.Button('OK', size=(10,1), pad=((5, 5)), disabled=True,), sg.Button('Clear', key='Clear_Login_Data', size=(10,1))],    
    ]

    # Contains items for directory input of user in the window
    directory_input_message_size = 13   # adjut directoy input message size
    directory_input = [
        [sg.Text("Select a directory for transfer...", font=('Arial', directory_input_message_size))],
        [sg.Text('Folder Path:'), sg.Input('', key='-dir_input-')], 
        [sg.FolderBrowse(target='-dir_input-', size=(10,1), pad=(5,5)), 
            sg.Button('Open', size=(10,1), pad=(5, 5), disabled=True), 
            sg.Button('Clear', key='Clear_Directory', size=(10,1))],
    ]
    
    finalize_buttons = [
        [sg.Button("Transfer", size=(30,3), pad=((0, 50), (0,0)), disabled= True), sg.Button("Cancel", size=(30,3))]    # Button for executing transfer           
    ]

    login_data_frame = sg.Frame('Log In', login_data, pad=((0,0) , (0,50)))
    directory_input_frame = sg.Frame('Open Directory', directory_input, pad=((0,0) , (0,50)))
    # Combined window layout
    transfer_data_layout = [
        [header],
        [login_data_frame],
        [directory_input_frame],
        [finalize_buttons]
    ]    
    
    # Window
    transfer_data_window = sg.Window("Transfer Data", transfer_data_layout, size=(
        1200, 800), element_justification='c', finalize=True, grab_anywhere=True) 

    # Event loop    
    while True:
        event, values = transfer_data_window.read()
            
        if event == sg.WIN_CLOSED:    # completely close program if 'x' is clicked
            sys.exit()
        elif event == "Cancel":   # return to start screen
            break
        elif event == 'Clear_Login_Data':
            transfer_data_window['-host_input-'].update('')
            transfer_data_window['-name_input-'].update('')
            transfer_data_window['-key_input-'].update('')
            transfer_data_window['-pass_input-'].update('')
            sg.popup('Login Data Cleared')
        elif event == 'Clear_Directory':
            transfer_data_window['-dir_input-'].update('')
            sg.popup('Directory Cleared')
        elif event == 'Transfer':
            selected_directory = values['-dir_input-']
            if is_valid_directory(selected_directory):
                sg.popup(f'Selected folder: {selected_directory}')
            else:
                sg.popup('Invalid directory. Please select a valid directory.')
                transfer_data_window['-dir_input-'].update('')

    window1.un_hide()
    transfer_data_window.close()

