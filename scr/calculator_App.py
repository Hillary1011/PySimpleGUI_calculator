import PySimpleGUI as sg


def display(theme):
    sg.theme(theme)
    sg.set_options(font="Franklin 14")
    layout = [
            [sg.Text("*"*7), sg.Text("Hillary.K.M", text_color="White", font="Magneto"), sg.Text("*"*7)], #Gigi   Forte
            [sg.Push(), sg.Text("", key="-FULL_OPERATION-", font="Franklin 10", background_color="white", text_color="Black")],
            [sg.Text("Text", key="-TEXT-", background_color="white",text_color="Black", justification="right", expand_x=True)],
            [sg.Push(), sg.Text("Theme", right_click_menu=theme_menu)],
            [sg.Button("Clear", expand_x=True), sg.Button("Clear", expand_x=True)],
            [sg.Button("7", size=(6, 3)), sg.Button("8", size=(6, 3)), sg.Button("9", size=(6, 3)), sg.Button("*", size=(6, 3))],
            [sg.Button("4", size=(6, 3)), sg.Button("5", size=(6, 3)), sg.Button("6", size=(6, 3)), sg.Button("/", size=(6, 3))],
            [sg.Button("1", size=(6, 3)), sg.Button("2", size=(6, 3)), sg.Button("3", size=(6, 3)), sg.Button("+", size=(6, 3))],
            [sg.Button("0", size=(6, 3)), sg.Button(".", size=(6, 3)), sg.Button("-", size=(6, 3)), sg.Button("=", size=(6, 3))]]

    return sg.Window("Calculator", layout)


theme_menu = ["menu", ["TanBlue", "Dark", "DarkGray8", "DarkAmber", "DarkPurple4", "random"]] # DarkAmber DarkPurple4 BluePurple DarkBlue17
window = display("Dark")

current_num = []
full_operation = []
# num_string = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]: # Checking for theme update
        window.close()
        window = display(event)
        # if len(current_num) != 0:
        #     window["-TEXT-"].update(num_string)
        print(event)

    if event in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
        # print(event, len(current_num))
        if event == '.' and len(current_num) != 0:
            print("pass")
            if '.' not in current_num:
                current_num.append(".")
                num_string = ''.join(current_num)
                window["-TEXT-"].update(num_string)
            else:
                pass # error double .
        else:
            if event != '.': # preventing . at the beginning of digits
                current_num.append(event)
                num_string = ''.join(current_num)
                window["-TEXT-"].update(num_string)
        # print(num_string)

    if event in ['*', '/', '+', '-'] and len(window["-TEXT-"].get()) != 0:
        if len(current_num) != 0:
            full_operation.append(''.join(current_num))
            current_num = []
            full_operation.append(event)
            window["-TEXT-"].update("")
            print(full_operation)
            full_operation_text = ''.join(full_operation).replace("/", "÷")
            window["-FULL_OPERATION-"].update(full_operation_text.replace("*", "×"))
            # print(len(window["-TEXT-"].get()))


    if event == "=":
        if len(current_num) != 0:
            full_operation.append("".join(current_num))
            print(full_operation)
            full_operation_text = ''.join(full_operation).replace("/", "÷")
            if full_operation[-1] not in ['*', '/', '+', '-'] and len(full_operation) >= 3:
                window["-FULL_OPERATION-"].update(full_operation_text.replace("*", "×"))
                result = eval(' '.join(full_operation))
                window["-TEXT-"].update(result)
        full_operation = []
        current_num = []
        window["-TEXT-"].update()
window.close()