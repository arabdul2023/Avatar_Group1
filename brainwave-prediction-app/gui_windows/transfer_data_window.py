import PySimpleGUI as sg
import sys
import os

def transfer_data_window(window1):

    # Open sftp for file transfers
    file_path = "../file-transfer/sftp.py"
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()

    title_font_size = 35   # adjust title font size
    info_text_size = 13   # adjut directoy input message size

    top_left = [ ]

    header = [
        [sg.Text("Transfer Data Screen", font=('Arial', title_font_size), justification='c', 
            pad=((0,0),(50,50)), auto_size_text=True)]    
    ]

    login_data = [
        [sg.Text('Login before selecting a directory', font=('Arial', info_text_size))],
        [sg.Text('Host:\t   '), sg.Input('', key='-host_input-', enable_events=True)],
        [sg.Text('User Name:'), sg.Input('', key='-name_input-', enable_events=True)],
        [sg.Text('Private Key:'), sg.Input('', key='-key_input-', password_char='*', enable_events=True)],
        [sg.Text('Password:  '), sg.Input('', key='-pass_input-', password_char='*', enable_events=True)],
        [sg.Button('OK', size=(10,1), pad=(5, 5), disabled=True, key='-ok_button-'),
            sg.Button('Disconnect', size=(10,1), pad=(5,5), disabled=True, key='-disconnect_button-'),
            sg.Button('Clear', key='-clear_login_data_button-', size=(10,1))],
        [sg.Text('Disconnected', key='-connectivity_text-', font='Arial', text_color='dark red')]
    ]

    # Contains items for directory input of user in the window
    directory_input = [
        [sg.Text("Select a directory for transfer", font=('Arial', info_text_size))],
        [sg.Text('Directory Path:'), sg.Input('', key='-dir_input-', enable_events=True, disabled=True)], 
        [sg.FolderBrowse(target='-dir_input-', size=(10,1), pad=(5,5), disabled=True, key='-browse_button-'), 
            sg.Button('Open', size=(10,1), pad=(5, 5), disabled=True, key='-open_button-'), 
            sg.Button('Clear', key='-clear_directory_button-', disabled=True, size=(10,1))],
        [sg.Text('Directory: ', key='-directory_text-', font='Arial')]
    ]
    
    finalize_buttons = [
        [sg.Button("Transfer", size=(30,3), pad=((0, 50), (0,0)), disabled= True, key='-transfer_button-'), 
            sg.Button("Exit", size=(30,3), key='-exit_button-')]    # Button for executing transfer           
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

    login_successful = False
    dir_opened_successful = False
 
    # Functions related to Login Frame events
    def check_login_fields():
        if (values['-host_input-'] != '') and (values['-name_input-'] != '') and (values['-key_input-'] != '') and (values['-pass_input-'] != ''):
            transfer_data_window['-ok_button-'].update(disabled=False)
        else:
            transfer_data_window['-ok_button-'].update(disabled=True)
    def logged_in_successfully():
        transfer_data_window['-connectivity_text-'].update('Connected', text_color='dark green')
        transfer_data_window['-dir_input-'].update(disabled=False)
        transfer_data_window['-browse_button-'].update(disabled=False)
        transfer_data_window['-clear_directory_button-'].update(disabled=False)
        transfer_data_window['-disconnect_button-'].update(disabled=False)
        transfer_data_window['-clear_login_data_button-'].update(disabled=True)
    def attempt_login():
        sg.popup('Logged in')
        login_successful = True
        if login_successful:
            logged_in_successfully()
        else:
            sg.popup('Unable to connect')        
    def clear_login_inputs():
        transfer_data_window['-host_input-'].update('')
        transfer_data_window['-name_input-'].update('')
        transfer_data_window['-key_input-'].update('')
        transfer_data_window['-pass_input-'].update('')
        transfer_data_window['-ok_button-'].update(disabled=True)
        transfer_data_window['-host_input-'].set_focus()
    def disconnected():
        login_successful=False
        folder_opened_successful=False
        clear_login_inputs()
        transfer_data_window['-connectivity_text-'].update('Disconnected', text_color='dark red')
        transfer_data_window['-disconnect_button-'].update(disabled=True)
        transfer_data_window['-clear_login_data_button-'].update(disabled=False)
        transfer_data_window['-dir_input-'].update('')
        transfer_data_window['-dir_input-'].update(disabled=True)
        transfer_data_window['-browse_button-'].update(disabled=True)
        transfer_data_window['-clear_directory_button-'].update(disabled=True)
        transfer_data_window['-directory_text-'].update('Directory: ')
        
        
    # Functions related to Directory Frame events    
    def check_directory_field():
        if (values['-dir_input-'] != ''):
            transfer_data_window['-open_button-'].update(disabled=False)
        else:
            transfer_data_window['-open_button-'].update(disabled=True)
    def is_valid_directory(input_value):
        return os.path.isdir(input_value)
    def open_directory(directory):
        if is_valid_directory(directory):
            dir_opened_successful=True
            newly_opened_directory = f'{directory}'
            transfer_data_window['-directory_text-'].update('Directory: ' + newly_opened_directory)
            transfer_data_window['-transfer_button-'].update(disabled=False)
        else:
            sg.popup('Invalid directory. Please select a valid directory.')
            transfer_data_window['-dir_input-'].update('')
            transfer_data_window['-open_button-'].update(disabled=True)
    def clear_directory_field():
        transfer_data_window['-dir_input-'].update('')
        transfer_data_window['-open_button-'].update(disabled=True)
 
    def transfer_file():
        sg.popup('Transfered')
        
        
    # Event loop    
    while True:
        event, values = transfer_data_window.read()
            
        if event == sg.WIN_CLOSED:    # completely close program if 'x' is clicked
            sys.exit()
        elif event in ('-host_input-','-name_input-','-key_input-','-pass_input-'):
            check_login_fields()
        elif event == '-ok_button-':
            attempt_login()
        elif event == '-disconnect_button-':
            disconnected()
        elif event == '-clear_login_data_button-':
            clear_login_inputs()
        elif event in ('-dir_input-'):
            check_directory_field()
        elif event == '-open_button-':
            open_directory(values['-dir_input-'])
        elif event == '-clear_directory_button-':
            clear_directory_field()
        elif event == '-transfer_button-':
            transfer_file()
        elif event == "-exit_button-":   # return to start screen
            file.close()
            break

    window1.un_hide()
    transfer_data_window.close()

