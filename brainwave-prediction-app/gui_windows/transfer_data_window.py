import PySimpleGUI as sg
import sys

def transfer_data_window(items, get_drone_action, window1):

    # Layout
    header_font_size = 20
    header = [
        [sg.Text("Transfer Data Screen", font=('Arial', header_font_size), justification='c', auto_size_text=True)],
    ]    

    transfer_data_layout = [
        [sg.Button('Home', size=(8, 2), image_filename="../brainwave-prediction-app/images/home.png"), sg.Push()], 
        [sg.Column(header, pad=((0, 55), (0, 0)))],
        [sg.Text("Locally stored directory")],
        [sg.Button('File Path'), sg.Input(key='-file_input-')],
        [sg.Button("OK", size=(10,1))], 
    ]    
        
    transfer_data_window = sg.Window("Transfer Data", transfer_data_layout, size=(
        1200, 800), element_justification='c', finalize=True)
    
    
    while True:
        event, values = transfer_data_window.read()
            
        if event == sg.WIN_CLOSED:
            sys.exit()
            break
        elif event == "Home":
            break
        elif event == "OK":
            sg.popup("Button OK was clicked!")
            
    window1.un_hide()
    transfer_data_window.close()