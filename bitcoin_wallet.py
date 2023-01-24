#https://tirinox.ru/send-bitcoin-over-python/?ysclid=lb1xuaxi9z988165321
#python -m nuitka hello.py
#mxMiDSUi1W3udhZjLkpbQ7mvNSRySqPePt
#cUJUwC5jqY5jFSFrtUKMDEfJocLYCNetQt65XnzJqxtC3GyHqhNS

#n1Xm8M4WbdV1QY8CquvxsFwkpAgSxUGryy
#cVumRHmC4gTZmzonHumLMmRnNrKKeXzYbEN6Z8PpSCNTh2tYqqHu
from tkinter import *
from tkinter import ttk

import serial.tools.list_ports
import serial

from bit import PrivateKey as Key
import bit

import cryptocode

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
wallet_add_entry = 0
wallet_state_add_label = 0

public_addres_wallet = 0
private_key_wallet = 0
wallet_state_label = 0
newWindow = 0
newWallet = 0

lang_var = 0

var_net=IntVar()
var_net.set(0)


def handle_click():
    global state, connect_port, enter_pin, s, frame2

    try:
        s = serial.Serial(port=connect_port, baudrate=9600,write_timeout=1, timeout=3)
    except:
        s.close()
        if lang_var == 0:
            state.set("Не удалось подключится")
        else:
            state.set("Dont connect")
    else:
        s.flushInput()
        s.flushOutput()
        s.write(str.encode("START\n"))
        data = s.readline(200)
        print(data)
        if len(data) != 0:
            if lang_var == 0:
                state.set("Подключенно")
            else:
                state.set("Connect")
        else:
            if lang_var == 0:
                state.set("Устройство не отвечает")
            else:
                state.set("Device dont reply")


    #res = s.read()
    #print(res)

def pin_handler():
    global current_state_label, s, private_key_wallet, public_addres_wallet
    pin = enter_pin.get()
    try:
        s.write(str.encode("GET\n"))
    except:
        if lang_var == 0:   
            current_state_label["text"] = "Не удалось подключится"
        else:
            current_state_label["text"] = "Dont connect"
        return 
    s.timeout = 5
    s.flushInput()
    s.flushOutput()
    data = s.readline(200)
    if len(data) != 0:
        if str(data[:-2], "ascii") == "EMPTY":
            if lang_var == 0:
                state.set("Кошклек пуст")
            else:
                state.set("Wallet empty")
            private_key_wallet = 0
            public_addres_wallet = 0
            if lang_var == 0:
                public_key_label["text"] = "Публичный номер кошелька " + str(0) 
                private_key_label["text"] =  "Приватный ключ кошелька " + str(0) 
            else:
                public_key_label["text"] = "Public wallet key " + str(0) 
                private_key_label["text"] =  "Private wallet key " + str(0) 
            return
        print(data)
        state.set("Подключенно")
        if lang_var == 0:
            current_state_label["text"] = "Кошелек загружен"
        else:
            current_state_label["text"] = "Wallet load"
        wallet = cryptocode.decrypt(str(data[:-2], "ascii"), str(pin))
        if wallet != False:
            private_key_wallet = wallet
        else:
            state.set("Не верный ПИН")
            private_key_wallet = 0
            public_addres_wallet = 0
            if lang_var == 0:
                public_key_label["text"] = "Публичный номер кошелька " + str(0) 
                private_key_label["text"] =  "Приватный ключ кошелька " + str(0) 
            else:
                public_key_label["text"] = "Public wallet key " + str(0) 
                private_key_label["text"] =  "Private wallet key " + str(0) 
            return
        print(private_key_wallet)
        update_balance()
        try:
            if var_net.get() == 0:
                k = bit.PrivateKeyTestnet(private_key_wallet)
            else:
                k = Key(private_key_wallet)
        except:
            state.set("Не верный ПИН")
            return
        state.set("Кошелек загружен")
        update_balance()
        public_addres_wallet = k.address
        if lang_var == 0:
            public_key_label["text"] = "Публичный номер кошелька " + str(public_addres_wallet) 
            private_key_label["text"] =  "Приватный ключ кошелька " + str(private_key_wallet) 
        else:
            public_key_label["text"] = "Public wallet key " + str(public_addres_wallet) 
            private_key_label["text"] =  "Private wallet key " + str(private_key_wallet) 
    else:
        if lang_var == 0:
            state.set("Не верный ПИН")
            current_state_label["text"] = "Не верный ПИН"
        else:
            state.set("Incorrect PIN")
            current_state_label["text"] = "Incorrect PIN"


def selected(event):
    global connect_port
    selected_indices = languages_listbox.curselection()
    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indices])
    selected_langs = selected_langs[:selected_langs.find(" ")]
    connect_port = selected_langs

def send_money():
    global public_addres_wallet, private_key_wallet, var_net, lang_var
    global wallet_entry, wallet_sum_entry, wallet_info_label, wallet_state_label, newWindow

    wallet_state_label["text"] = "" 
    newWindow.update()

    destination = wallet_entry.get()
    summ =  wallet_sum_entry.get()

    if var_net.get() == 0:
        source_k = bit.PrivateKeyTestnet(private_key_wallet)
    else:
        source_k = Key(private_key_wallet)

    print(f'Send from {str(public_addres_wallet)} to {destination}')
    try:
        r = source_k.send([
        (destination, float(summ), 'btc')
        ])
    except:
        print("wrong transaction")
        if lang_var == 0:
            wallet_state_label["text"] = "Транзакция не прошла" 
        else:
            wallet_state_label["text"] = "Wrong transaction" 
    else:
        if lang_var == 0:
            wallet_state_label["text"] = "Транзакция прошла. \n " + str(r)
        else:
            wallet_state_label["text"] = "Success. \n " + str(r)
        print(r)  # ID транзакции
        update_balance()


def transmit_money():
    global wallet_entry, wallet_sum_entry, wallet_info_label, wallet_state_label, newWindow, lang_var
    newWindow = Tk()

    if lang_var == 0:
        number = "Номер вашего кошелька "
        number_reciever = "Номер кошелька назначение"
        summa = "Сумма"
        but = "Отправить"
    else:
        number = "Your wallet "
        number_reciever = "Destination wallet"
        summa = "Amount"
        but = "Send"
    my_wallet_label = ttk.Label(newWindow, text = number +str( public_addres_wallet))
    my_wallet_label.pack()

    wallet_info_label = ttk.Label(newWindow, text = number_reciever)
    wallet_info_label.pack()
    wallet_entry = Entry( master = newWindow, width=50)
    wallet_entry.pack()

    wallet_sum_label = ttk.Label(newWindow, text = summa)
    wallet_sum_label.pack()
    wallet_sum_entry = Entry( master = newWindow, width=50)
    wallet_sum_entry.pack()

    wallet_send_button = ttk.Button(newWindow, text = but, command=send_money)
    wallet_send_button.pack(padx=5, pady=20)

    wallet_state_label = ttk.Label(newWindow)
    wallet_state_label.pack(padx=5, pady=10)

def recieve_money():
    global public_addres_wallet

    recieve = Tk()

    public_text_wallet = Text(recieve, height=1, borderwidth=0)
    public_text_wallet.insert(1.0, str(public_addres_wallet))
    public_text_wallet.pack()

def get_private_key():
    global private_key_wallet

    recieve = Tk()

    public_text_wallet = Text(recieve, height=1, borderwidth=0)
    public_text_wallet.insert(1.0,  str(private_key_wallet))
    public_text_wallet.pack()
    
def erase_wallet():
    global s, current_state_label, lang_var
    s.flushInput()
    s.flushOutput()
    try:
        s.write(str.encode("ERASE_ALL"))
    except:
        if lang_var == 0:
            current_state_label["text"] = "Не подключенно!"
        else:
            current_state_label["text"] = "Disconnect"
        return
    s.timeout = 5
    s.flushInput()
    s.flushOutput()
    data = s.readline(200)
    if len(data) != 0:
        if lang_var == 0:
            state.set("Кошелек очищен")
        else:
            state.set("Wallet clear")

def save_wallet():
    global s, private_key_wallet, current_state_label
    print(str.encode("SAVE" + private_key_wallet + "\r\n"))
    s.flushInput()
    s.flushOutput()
    pin = enter_pin.get()
    str_encoded = cryptocode.encrypt(private_key_wallet,str(pin))
    try:
        s.write(str.encode("SAVE" + str_encoded + "\r\n"))
    except:
        if lang_var == 0:
            current_state_label["text"] = "Не подключенно!"
        else:
            current_state_label["text"] = "Dont connect!"
        return
    s.timeout = 5
    s.flushInput()
    s.flushOutput()
    data = s.readline(200)
    if len(data) != 0:
        if lang_var == 0:
            state.set("Кошелек сохранен")
        else:
            state.set("Wallet save")
        
def set_new_wallet():
    global wallet_add_entry, private_key_wallet, public_addres_wallet, wallet_state_add_label, var_net, newWallet

    wallet_state_add_label["text"] = " "

    private_key_wallet = wallet_add_entry.get()
    try:
        if var_net.get() == 0:
            k = bit.PrivateKeyTestnet(private_key_wallet)
        else:
            k = Key(private_key_wallet)
    except:
        if lang_var == 0:
            wallet_state_add_label["text"] = "Неправильный номер кошелька"
        else:
            wallet_state_add_label["text"] = "Incorrect key wallet"
        return

    print('Public address:', k.address)
    public_addres_wallet = k.address
    if lang_var == 0:
        public_key_label["text"] = "Публичный номер кошелька " + str(public_addres_wallet) 
        private_key_label["text"] =  "Приватный ключ кошелька " + str(private_key_wallet) 
    else:
        public_key_label["text"] = "Public wallet key " + str(public_addres_wallet) 
        private_key_label["text"] =  "Private wallet key " + str(private_key_wallet) 
    if lang_var == 0:
        wallet_state_add_label["text"] = "Кошелек добавлен"
    else:
        wallet_state_add_label["text"] = "Wallet commit"

    newWallet.destroy()



def add_wallet():
    global wallet_add_entry, wallet_state_add_label, newWallet

    newWallet= Tk()

    if lang_var == 0:
        wallet_info = "Введите приватный номер кошелька"
        add_but = "Добавить"
    else:
        wallet_info = "Insert private key wallet"
        add_but = "Add"      

    wallet_info_add_label = ttk.Label(newWallet, text = wallet_info)
    wallet_info_add_label.pack()
    wallet_add_entry = Entry( master = newWallet, width=50)
    wallet_add_entry.pack()

    wallet_send_button = ttk.Button(newWallet, text = add_but, command=set_new_wallet)
    wallet_send_button.pack()   

    wallet_state_add_label = ttk.Label(newWallet)
    wallet_state_add_label.pack()

def create_wallet():
    global wallet_my, public_addres_wallet, private_key_wallet, var_net
    print(var_net)
    if var_net.get() == 0:
        k = bit.PrivateKeyTestnet()
        print("test_net")
    else:
        k = Key()
    wallet_my = k.to_wif()
    print('Private key:', k.to_wif())
    print('Public address:', k.address)
    private_key_wallet = k.to_wif()
    public_addres_wallet = k.address

    if lang_var == 0:
        public_key_label["text"] = "Публичный номер кошелька " + str(public_addres_wallet) 
        private_key_label["text"] =  "Приватный ключ кошелька " + str(private_key_wallet) 
    else:
        public_key_label["text"] = "Public wallet key " + str(public_addres_wallet) 
        private_key_label["text"] =  "Private wallet key " + str(private_key_wallet) 


def handle_update():
    global ports, languages_var
    ports = serial.tools.list_ports.comports(include_links=False)
    languages_var = Variable(value=ports)
    languages_listbox.delete(0, END)  #clear listbox
    for filename in ports: #populate listbox again
        languages_listbox.insert(END, filename)

def handle_close():
    global s
    global state, lang_var
    if lang_var == 0:
        state.set("Отключенно")
    else:
        state.set("Disconnect")
    s.close()


def update_balance_thread():
    global private_key_wallet, var_net
    if var_net.get() == 0:
        k = bit.PrivateKeyTestnet(private_key_wallet)
    else:
        k = Key(private_key_wallet)
    balance = k.get_balance()
    print(balance) 
    account_label["text"] = balance

def update_balance(): 
    th = Thread(target=update_balance_thread, args=())
    th.start()

def lang_click():
    global lang_var
    
    if lang_var == 0:
        lang_var = 1
        state_label["text"] = "State"
        vary_blockcahain_label["text"] = "Set blockchain"
        lang_button.config(text="Русский")  
        rad0.config(text="Test")
        rad1.config(text="True")
        public_key_label["text"] = "Public key "
        private_key_label["text"] = "Private key "
        connect_button.config(text="Connect")
        update_button.config(text="Refresh")
        close_button.config(text="Disconnect")
        balance_label["text"] = "Balance"
        update_balance_button.config(text="Update balance")
        pin_label["text"] = "Enter PIN"
        pin_button.config(text="Load wallet")
        transmit_money_button.config(text="Send money")
        recieve_money_button.config(text="Get public key")
        recieve_private_button.config(text="Get private key")
        creat_wallet_button.config(text="Create wallet")
        add_wallet_button.config(text="Add wallet")
        erase_wallet_button.config(text="Erase wallet")
        save_wallet_button.config(text="Save wallet")
        button_exit.config(text="Exit")
    else:
        lang_var = 0
        state_label["text"] = "Состояние"
        vary_blockcahain_label["text"] = "Выбор сети"
        lang_button.config(text="English")
        rad0.config(text="Тестовая")
        rad1.config(text="Настоящая")
        public_key_label["text"] = "Публичный номер кошелька "
        private_key_label["text"] = "Приватный ключ кошелька "
        connect_button.config(text="Подключится")
        update_button.config(text="Обновить")
        close_button.config(text="Отключится")
        balance_label["text"] = "Баланс"
        update_balance_button.config(text="Обновить баланс")
        pin_label["text"] = "Введите ПИН"
        pin_button.config(text="Загрузить кошелек")
        transmit_money_button.config(text="Перевести")
        recieve_money_button.config(text="Получить публичный ключ")
        recieve_private_button.config(text="Получить приватный ключ")
        creat_wallet_button.config(text="Создать кошелек")
        add_wallet_button.config(text="Добавить кошелек")
        erase_wallet_button.config(text="Удалить кошелек")
        save_wallet_button.config(text="Сохранить кошелек")
        button_exit.config(text="Выход")

#ttk.Label(frm, text="ВВедите пин").grid(column=0, row=0)
frame1 = ttk.Frame(master=root, width=300, height=50,)
frame1.pack(fill=Y, side=LEFT, expand=False)
state_label = ttk.Label(master = frame1, text="Состояние:")
state_label.pack(anchor=NW, fill=Y, padx=5, pady=5)

current_state_label = ttk.Label(master = frame1, textvariable=state)
current_state_label.pack(anchor=NW, fill=Y, padx=5, pady=5)

vary_blockcahain_label = ttk.Label(master = frame1, text="Выбор сети")
vary_blockcahain_label.pack(anchor=NW, fill=Y, padx=5, pady=20)
rad0 = Radiobutton(frame1, text="Тестовая", variable=var_net, value=0)
rad0.pack(anchor=NW, fill=Y, padx=5, pady=5)
rad1 = Radiobutton(frame1, text="Настоящая", variable=var_net, value=1)
rad1.pack(anchor=NW, fill=Y, padx=5, pady=5)

lang_label = ttk.Label(master = frame1, text="Language:")
lang_label.pack(anchor=NW, fill=Y, padx=5, pady=5)
lang_button = ttk.Button(frame1, text="English", command=lang_click)
lang_button.pack(anchor=NW, fill=X, padx=5, pady=5)

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

update_button = ttk.Button(frame3, text="Обновить", command=handle_update)
update_button.pack(anchor=NW, fill=X, padx=5, pady=5)

close_button = ttk.Button(frame3, text="Отключится", command=handle_close)
close_button.pack(anchor=NW, fill=X, padx=5, pady=5)


frame2 = ttk.Frame(master=root, width=100, height=100,)
frame2.pack(fill=Y, side=LEFT)
balance_label = ttk.Label(master = frame2, text="Баланс:")
balance_label.pack(anchor=NW, fill=Y, padx=50, pady=5)

account_label = ttk.Label(master = frame2, text="0")
account_label.pack(anchor=NW, fill=Y, padx=50, pady=5)

update_balance_button = ttk.Button(frame2, text="Обновить баланс", command=update_balance)
update_balance_button.pack(anchor=NW, fill=X, padx=50, pady=5)

pin_label = ttk.Label(master = frame2, text="Введите ПИН")
pin_label.pack(anchor=NW, fill=X, padx=50, pady=5)
enter_pin = Entry( master = frame2, width=5)
enter_pin.pack(anchor=NW, fill=X, padx=50, pady=5)
pin_button = ttk.Button(frame2, text="Загрузить кошелек", command=pin_handler)
pin_button.pack(anchor=NW, fill=X, padx=50, pady=5)


frame4 = ttk.Frame(master=root, width=100, height=100,)
frame4.pack(fill=Y, side=LEFT)

transmit_money_button = ttk.Button(frame4, text="Перевести", command=transmit_money)
transmit_money_button.pack(anchor=NW, fill=X, padx=50, pady=5)

recieve_money_button = ttk.Button(frame4, text="Получить публичный ключ", command=recieve_money)
recieve_money_button.pack(anchor=NW, fill=X, padx=50, pady=5)

recieve_private_button = ttk.Button(frame4, text="Получить приватный ключ", command=get_private_key)
recieve_private_button.pack(anchor=NW, fill=X, padx=50, pady=5)

creat_wallet_button = ttk.Button(frame4, text="Создать кошелек", command=create_wallet)
creat_wallet_button.pack(anchor=NW, fill=X, padx=50, pady=5)

add_wallet_button = ttk.Button(frame4, text="Добавить кошелек", command=add_wallet)
add_wallet_button.pack(anchor=NW, fill=X, padx=50, pady=5)

erase_wallet_button = ttk.Button(frame4, text="Удалить кошелек", command=erase_wallet)
erase_wallet_button.pack(anchor=NW, fill=X, padx=50, pady=5)

save_wallet_button = ttk.Button(frame4, text="Сохранить кошелек", command=save_wallet)
save_wallet_button.pack(anchor=NW, fill=X, padx=50, pady=5)

button_exit = ttk.Button(frame4, text="Выход", command=root.destroy)
button_exit.pack(anchor=NW, fill=X, padx=50, pady=5)


root.mainloop()