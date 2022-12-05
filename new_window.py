from tkinter import *
from tkinter import ttk

import serial.tools.list_ports
import serial

root = Tk()
root.title("Bticoin Wallet")
root.maxsize(1000, 400)
root.minsize(400, 400)

ports = serial.tools.list_ports.comports(include_links=False)
languages_var = Variable(value=ports)

enter_pin = Entry( width=5)

state = StringVar()
state.set('Не подключенно')

connect_port = ""

s = serial.Serial()


def handle_click():
    global state, connect_port, enter_pin, s
    
    print("Нажата кнопка!")
    try:
        s = serial.Serial(port=connect_port, baudrate=9600)
    except:
        state.set("Ошибка!")
    else:
        state.set("Подключенно")
        pin_label = ttk.Label(master = root, text="ВВедите ПИН:")
        pin_label.pack(anchor=NW, fill=X, padx=5, pady=5)
        enter_pin.pack(anchor=NW, fill=X, padx=5, pady=5)
        pin_button = ttk.Button(root, text="Ввести ПИН", command=pin_handler)
        pin_button.pack(anchor=NW, fill=X, padx=5, pady=5)

    #res = s.read()
    #print(res)

def pin_handler():
    pin = enter_pin.get()
    print(pin)
    s.writelines(str.encode(pin))

def selected(event):
    # получаем индексы выделенных элементов
    global connect_port
    selected_indices = languages_listbox.curselection()
    # получаем сами выделенные элементы
    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indices])
    msg = f"вы выбрали: {selected_langs}"
    selection_label["text"] = msg
    selected_langs = selected_langs[:selected_langs.find(" ")]
    connect_port = selected_langs
 

#ttk.Label(frm, text="ВВедите пин").grid(column=0, row=0)
frame1 = ttk.Frame(master=root)
frame1.pack(fill=Y, side=LEFT)
state_label = ttk.Label(master = frame1, text="Состояние:")
state_label.pack(anchor=NW, fill=Y, padx=5, pady=5)

current_state_label = ttk.Label(master = frame1, textvariable=state)
current_state_label.pack(anchor=NW, fill=Y, padx=5, pady=5)

languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
languages_listbox.bind("<<ListboxSelect>>", selected)

connect_button = ttk.Button(root, text="Подключится", command=handle_click)
connect_button.pack(anchor=NW, fill=X, padx=5, pady=5)



selection_label = ttk.Label()
selection_label.pack(anchor=NW, fill=X, padx=5, pady=5)

button_exit = ttk.Button(root, text="Выход", command=root.destroy)
button_exit.pack(anchor=NW, fill=X, padx=5, pady=5)
#button = Button(frm, text="Кликни!", command=handle_click).grid(column=0, row=3)


 

 

 
root.mainloop()