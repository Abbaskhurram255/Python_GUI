from FreeSimpleGUI import *

theme("Reds")

lay = [
    [Text("Please fill the following fields:")],
    [T("Name", size=(15,2)), I(key="name")],
    [T("Password", size=(15, 2)), I(key="pwd")],
    [Submit(), Exit()]
]


window = Window("Simple Data Entry Form", lay)

while True:
    event, values = window.read()
    if event == WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        print("Event: "+event)
        print("Name="+values["name"])
        print("Password="+values["name"])
window.close()
