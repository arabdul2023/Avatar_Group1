import PySimpleGUI as sg
import sys
import os

sys.path.append('../file-transfer')
from sftp import fileTransfer as ft

def transfer_data_window(window1):

    title_font_size = 35   # adjust title font size
    info_text_size = 13   # adjut directoy input message size

    top_left = [ ]

    header = [
        [sg.Text("Transfer Data Screen", font=('Arial', title_font_size), justification='c', 
            pad=((0,0),(10,10)), auto_size_text=True)]    
    ]

    login_data = [
        [sg.Text('Login before selecting a directory', font=('Arial', info_text_size))],
        [sg.Text('Host:\t   '), sg.Input('', size=(57,1), key='-host_input-', enable_events=True)],
        [sg.Text('User Name:'), sg.Input('', size=(57,1), key='-name_input-', enable_events=True)],
        [sg.Text('Private Key:'), sg.Input('', size=(57,1), key='-key_input-', password_char='*', enable_events=True)],
        [sg.Text('Password:   '), sg.Input('', size=(57,1), key='-pass_input-', password_char='*', enable_events=True)],
        [sg.Button('Login', size=(10,1), pad=(5, 5), disabled=True, key='-login_button-'),
            sg.Button('Disconnect', size=(10,1), pad=(5,5), disabled=True, key='-disconnect_button-'),
            sg.Button('Clear', key='-clear_login_data_button-', size=(10,1))],
        [sg.Text('Disconnected', key='-connectivity_text-', font='Arial', text_color='dark red')]
    ]

    # Contains items for directory input of user in the window
    directory_input = [
        # Origin Directory
        [sg.Text("Select an origin directory for transfer", font=('Arial', info_text_size))],
        [sg.Text('Origin Path:'), sg.Input('', size=(57,1), key='-origin_dir_input-', enable_events=True, disabled=True)], 
        [sg.FolderBrowse(target='-origin_dir_input-', size=(10,1), pad=(5,5), disabled=True, key='-origin_browse_button-'), 
            sg.Button('Select', size=(10,1), pad=(5, 5), disabled=True, key='-origin_open_button-'), 
            sg.Button('Clear', key='-clear_origin_directory_button-', disabled=True, size=(10,1))],
        
        # Target Directory
        [sg.Text("Select a target directory for transfer", font=('Arial', info_text_size))],
        [sg.Text('Target Path:'), sg.Input('', size=(57,1), key='-target_dir_input-', enable_events=True, disabled=True)], 
        [sg.FolderBrowse(target='-target_dir_input-', size=(10,1), pad=(5,5), disabled=True, key='-target_browse_button-'), 
            sg.Button('Select', size=(10,1), pad=(5, 5), disabled=True, key='-target_open_button-'), 
            sg.Button('Clear', key='-clear_target_directory_button-', disabled=True, size=(10,1))],

        # Currently selected directories
        [sg.Text('Origin: ', font='Arial'), sg.Text('', key='-origin_directory_text-', font='Arial')],
        [sg.Text('Target: ', font='Arial'), sg.Text('', key='-target_directory_text-', font='Arial')]    
    ]

    finalize_buttons = [
        [sg.Button("Transfer", size=(30,3), pad=((0, 21), (0,0)), disabled= True, key='-transfer_button-'), 
            sg.Button("Exit", size=(30,3), pad=((11, 0), (0,0)), key='-exit_button-')]    # Button for executing transfer           
    ]
    open_popups = []

    login_data_frame = sg.Frame('Log In', login_data, pad=((0,0) , (0,10)))
    directory_input_frame = sg.Frame('Directories', directory_input, pad=((0,0) , (0,10)))
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

    # Functions related to Login Frame events
    def check_login_fields():
        if (values['-host_input-'] != '') and (values['-name_input-'] != '') and (values['-key_input-'] != '') and (values['-pass_input-'] != ''):
            transfer_data_window['-login_button-'].update(disabled=False)
        else:
            transfer_data_window['-login_button-'].update(disabled=True)
    def enable_origin_directory():
        transfer_data_window['-origin_dir_input-'].update(disabled=False)
        transfer_data_window['-origin_browse_button-'].update(disabled=False)
        transfer_data_window['-clear_origin_directory_button-'].update(disabled=False)
    def enable_target_directory():
        transfer_data_window['-target_dir_input-'].update(disabled=False)
        transfer_data_window['-target_browse_button-'].update(disabled=False)
        transfer_data_window['-clear_target_directory_button-'].update(disabled=False)    
    def logged_in_successfully():
        transfer_data_window['-connectivity_text-'].update('Connected', text_color='dark green')
        transfer_data_window['-disconnect_button-'].update(disabled=False)
        transfer_data_window['-clear_login_data_button-'].update(disabled=True)
        enable_origin_directory()
        enable_target_directory()
    def attempt_login():
        #ft.host = values['-host_input-']
        #ft.username = values['-name_input-']
        #ft.private_key = values['-key_input-']
        #ft.private_key_pass = values['-pass_input-']
        #ft.port = 22
        #ft.connect(ft)
        
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
        transfer_data_window['-login_button-'].update(disabled=True)
        transfer_data_window['-host_input-'].set_focus()
    def disable_origin_directory():
        transfer_data_window['-origin_dir_input-'].update('')
        transfer_data_window['-origin_dir_input-'].update(disabled=True)
        transfer_data_window['-origin_browse_button-'].update(disabled=True)
        transfer_data_window['-origin_open_button-'].update(disabled=True)
        transfer_data_window['-clear_origin_directory_button-'].update(disabled=True)
        transfer_data_window['-origin_directory_text-'].update('')
    def disabel_target_directory():
        transfer_data_window['-target_dir_input-'].update('')
        transfer_data_window['-target_dir_input-'].update(disabled=True)
        transfer_data_window['-target_browse_button-'].update(disabled=True)
        transfer_data_window['-target_open_button-'].update(disabled=True)
        transfer_data_window['-clear_target_directory_button-'].update(disabled=True)
        transfer_data_window['-target_directory_text-'].update('')
    def disconnected():
        clear_login_inputs()
        disable_origin_directory()
        disabel_target_directory()
        transfer_data_window['-connectivity_text-'].update('Disconnected', text_color='dark red')
        transfer_data_window['-disconnect_button-'].update(disabled=True)
        transfer_data_window['-clear_login_data_button-'].update(disabled=False)
        
    # Functions related to Directory Frame events
    def is_valid_directory(input_value):
        return os.path.isdir(input_value)
    def check_directory_field(field, button):
        if (values[field] != ''):
            transfer_data_window[button].update(disabled=False)
        else:
            transfer_data_window[button].update(disabled=True)
    def open_directory(field, text, button):
        if is_valid_directory(values[field]):
            dir_opened_successful=True
            newly_opened_directory = f'{values[field][-52:]}'
            transfer_data_window[text].update("..." + newly_opened_directory)
            check_opened_directories()
        else:
            sg.popup('Invalid directory. Please select a valid directory.')
            transfer_data_window[field].update('')
            transfer_data_window[button].update(disabled=True)
            check_opened_directories()
    def clear_directory_field(field, button, text):
        transfer_data_window[field].update('')
        transfer_data_window[button].update(disabled=True)
        transfer_data_window[text].update('')
        check_opened_directories()

    def enable_transfer_button():
        transfer_data_window['-transfer_button-'].update(disabled=False)
    def disable_transfer_button():
        transfer_data_window['-transfer_button-'].update(disabled=True)        
    def check_opened_directories():
        #print(transfer_data_window['-origin_directory_text-'].get())
        #print(transfer_data_window['-target_directory_text-'].get())
        if(transfer_data_window['-origin_directory_text-'].get() != '') and (transfer_data_window['-target_directory_text-'].get() != ''):
            enable_transfer_button()
        else:
            disable_transfer_button()
    def transfer_file():
        print('ran')
        #ft.transfer(ft,to,fro) 
         
    # Event loop    
    while True:
        event, values = transfer_data_window.read()
            
        if event == sg.WIN_CLOSED:    # completely close program if 'x' is clicked
            sys.exit()
        elif event in ('-host_input-','-name_input-','-key_input-','-pass_input-'):
            check_login_fields()
        elif event == '-login_button-':
            attempt_login()
        elif event == '-disconnect_button-':
            disconnected()
        elif event == '-clear_login_data_button-':
            clear_login_inputs()
        elif event in ('-origin_dir_input-'):
            check_directory_field('-origin_dir_input-', '-origin_open_button-')
        elif event == '-origin_open_button-':
            open_directory('-origin_dir_input-', '-origin_directory_text-', '-origin_open_button-')
        elif event == '-clear_origin_directory_button-':
            clear_directory_field('-origin_dir_input-', '-origin_open_button-', '-origin_directory_text-')
        elif event in ('-target_dir_input-'):
            check_directory_field('-target_dir_input-', '-target_open_button-')
        elif event == '-target_open_button-':
            open_directory('-target_dir_input-', '-target_directory_text-', '-target_open_button-')
        elif event == '-clear_target_directory_button-':
            clear_directory_field('-target_dir_input-', '-target_open_button-', '-target_directory_text-')
        elif event == '-transfer_button-':
            result = sg.popup('Do you want to proceed?', title='Verify', button_type=sg.POPUP_BUTTONS_OK_CANCEL)
            if result == 'OK':
                transfer_file()
        elif event == "-exit_button-":   # return to start screen
            result = sg.popup('Do you want to proceed?', title='Verify', button_type=sg.POPUP_BUTTONS_OK_CANCEL)
            if result == 'OK':
                break

    window1.un_hide()
    transfer_data_window.close()

