import PySimpleGUI as sg

layout = [
    [sg.Text('Username:'), sg.InputText(key="-USERNAME-")],
    [sg.Text('Password:'), sg.InputText(key="-PASSWORD-")],
    [sg.OK()]
]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print("Username", values["-USERNAME-"])
    print("Password", values["-PASSWORD-"])

window.close()