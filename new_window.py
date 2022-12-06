#https://tirinox.ru/send-bitcoin-over-python/?ysclid=lb1xuaxi9z988165321
from tkinter import *
from tkinter import ttk

import serial.tools.list_ports
import serial

from bit import PrivateKey as Key

from threading import Thread

root = Tk()
root.title("Bticoin Wallet")
root.maxsize(1000, 400)
root.minsize(400, 400)

frame2 = 0
frame3 = 0
frame1 = 0

ports = serial.tools.list_ports.comports(include_links=False)
languages_var = Variable(value=ports)


state = StringVar()
state.set('Не подключенно')

connect_port = ""

s = serial.Serial()

wallet_my = 0
wallet_sum_entry = 0
wallet_info_label = 0

public_addres_wallet = 0
private_key_wallet = 0
wallet_state_label = 0

def handle_click():
    global state, connect_port, enter_pin, s, frame2

    try:
        s = serial.Serial(port=connect_port, baudrate=115200)
    except:
        state.set("Ошибка!")
    else:
        state.set("Подключенно")
        pin_label = ttk.Label(master = frame3, text="Введите ПИН:")
        pin_label.pack(anchor=NW, fill=X, padx=5, pady=5)
        enter_pin.pack(anchor=NW, fill=X, padx=5, pady=5)
        pin_button = ttk.Button(frame3, text="Ввести ПИН", command=pin_handler)
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
    #msg = f"вы выбрали: {selected_langs}"
    selection_label["text"] = selected_langs[:6]
    selected_langs = selected_langs[:selected_langs.find(" ")]
    connect_port = selected_langs

def send_money():
    global public_addres_wallet, private_key_wallet 
    global wallet_entry, wallet_sum_entry, wallet_info_label, wallet_state_label

    destination = wallet_entry.get()
    summ =  wallet_sum_entry.get()
    source_k = Key(private_key_wallet)
    '''
    try:
        dest_k = Key(destination)
    except:
        print("wrong wallet")
        wallet_state_label["text"] = "Неправильный номер кошелька"
        return
    else:
        wallet_state_label["text"] = " "
    '''
    print(f'Send from {public_addres_wallet} to {destination}')
    try:
        r = source_k.send([
        (destination, int(summ), 'btc')
        ])
    except:
        print("wrong transaction")
        wallet_state_label["text"] = "Транзакция не прошла" 
    else:
        wallet_state_label["text"] = "Транзакция прошла. \n " + str(r)
        print(r)  # ID транзакции


def transmit_money():
    global wallet_entry, wallet_sum_entry, wallet_info_label, wallet_state_label
    newWindow = Tk()

    my_wallet_label = ttk.Label(newWindow, text = "Номер моего кошелька " + public_addres_wallet)
    my_wallet_label.pack()

    wallet_info_label = ttk.Label(newWindow, text = "Номер кошелька")
    wallet_info_label.pack()
    wallet_entry = Entry( master = newWindow, width=50)
    wallet_entry.pack()

    wallet_sum_label = ttk.Label(newWindow, text = "Сумма")
    wallet_sum_label.pack()
    wallet_sum_entry = Entry( master = newWindow, width=50)
    wallet_sum_entry.pack()

    wallet_send_button = ttk.Button(newWindow, text = "Отправить", command=send_money)
    wallet_send_button.pack()

    wallet_state_label = ttk.Label(newWindow)
    wallet_state_label.pack()

def recieve_money():
    global private_key_wallet

    recieve = Tk()

    wallet_number_label = ttk.Label(recieve, text = "Номер кошелька " + public_addres_wallet)
    wallet_number_label.pack()

def create_wallet():
    global wallet_my, public_addres_wallet, private_key_wallet

    k = Key()
    wallet_my = k.to_wif()
    print('Private key:', k.to_wif())
    print('Public address:', k.address)
    private_key_wallet = k.to_wif()
    public_addres_wallet = k.address

    public_key_label["text"] = "Публичный номер кошелька " + str(public_addres_wallet) 
    private_key_label["text"] =  "Приватный ключ кошелька " + str(private_key_wallet) 

def update_balance_thread():
    global private_key_wallet
    k = Key(private_key_wallet)##public mwe1UYZXZ48nLnSr1H4TkVjasKVopHgRjc
    balance = k.get_balance()
    print(balance) 
    account_label["text"] = balance

def update_balance(): 
    th = Thread(target=update_balance_thread, args=())
    th.start()




#ttk.Label(frm, text="ВВедите пин").grid(column=0, row=0)
frame1 = ttk.Frame(master=root, width=100, height=50,)
frame1.pack(fill=Y, side=LEFT)
state_label = ttk.Label(master = frame1, text="Состояние:")
state_label.pack(anchor=NW, fill=Y, padx=5, pady=5)

current_state_label = ttk.Label(master = frame1, textvariable=state)
current_state_label.pack(anchor=NW, fill=Y, padx=5, pady=5)


frame5 = ttk.Frame(master=root)
frame5.pack(fill=X, side=BOTTOM)
public_key_label = ttk.Label(master = frame5, text= "Публичный номер кошелька " + str(public_addres_wallet) )
public_key_label.pack(anchor=NW, fill=Y, padx=5, pady=5)

private_key_label = ttk.Label(master = frame5, text= "Приватный ключ кошелька " + str(private_key_wallet) )
private_key_label.pack(anchor=NW, fill=Y, padx=5, pady=5)


frame3 = ttk.Frame(master=root, width=100, height=100,)
frame3.pack(fill=Y, side=LEFT)

languages_listbox = Listbox(master = frame3, listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
languages_listbox.bind("<<ListboxSelect>>", selected)

connect_button = ttk.Button(frame3, text="Подключится", command=handle_click)
connect_button.pack(anchor=NW, fill=X, padx=5, pady=5)

selection_label = ttk.Label(frame3)
selection_label.pack(anchor=NW, fill=X, padx=5, pady=5)

button_exit = ttk.Button(frame3, text="Выход", command=root.destroy)
button_exit.pack(anchor=NW, fill=X, padx=5, pady=5)

enter_pin = Entry( master = frame3, width=5)


frame2 = ttk.Frame(master=root, width=100, height=100,)
frame2.pack(fill=Y, side=LEFT)
balance_label = ttk.Label(master = frame2, text="Баланс:")
balance_label.pack(anchor=NW, fill=Y, padx=50, pady=5)

account_label = ttk.Label(master = frame2, text="0")
account_label.pack(anchor=NW, fill=Y, padx=50, pady=5)

update_balance_button = ttk.Button(frame2, text="Обновить баланс", command=update_balance)
update_balance_button.pack(anchor=NW, fill=X, padx=50, pady=5)


frame4 = ttk.Frame(master=root, width=100, height=100,)
frame4.pack(fill=Y, side=LEFT)

transmit_money_button = ttk.Button(frame4, text="Перевести", command=transmit_money)
transmit_money_button.pack(anchor=NW, fill=X, padx=50, pady=5)

recieve_money_button = ttk.Button(frame4, text="Пополнить", command=recieve_money)
recieve_money_button.pack(anchor=NW, fill=X, padx=50, pady=5)

creat_wallet_button = ttk.Button(frame4, text="Создать кошелек", command=create_wallet)
creat_wallet_button.pack(anchor=NW, fill=X, padx=50, pady=5)




root.mainloop()