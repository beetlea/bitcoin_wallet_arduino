#https://tirinox.ru/send-bitcoin-over-python/?ysclid=lb1xuaxi9z988165321
from bit import PrivateKey as Key
from tkinter import *
from tkinter import ttk
import serial.tools.list_ports
import serial

root = Tk()
root.title("Bticoin Wallet")
root.maxsize(1000, 400)
root.minsize(400, 400)
frm = ttk.Frame(root, padding=20)

ports = serial.tools.list_ports.comports(include_links=False)
'''
s = serial.Serial(port="COM4", baudrate=9600)
res = s.read()
print(res)
'''
state = StringVar()
state.set('Не подключенно')

def handle_click():
    global state
    state.set("Подключенно")
    print("Нажата кнопка!")

def listbox_select(event):
    selected_indices = listbox1.curselection()

languages_var = Variable(value=ports)

frm.grid()
#ttk.Label(frm, text="ВВедите пин").grid(column=0, row=0)
ttk.Label(frm, text="Состояние:").grid(column=1, row=0)
ttk.Label(frm, textvariable=state).grid(column=2, row=0)
ttk.Button(frm, text="Подключится", command=handle_click).grid(column=2, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=6)
#button = Button(frm, text="Кликни!", command=handle_click).grid(column=0, row=3)
 
listbox1=Listbox(frm,height=5,width=15, listvariable=languages_var, selectmode=EXTENDED).grid(column=2, row=3)
listbox1.bind("<<ListboxSelect>>", listbox_select)

enter_pin = Entry( width=5).grid(column=1, row=0)
print(enter_pin)
root.update()
root.mainloop()
'''
k = Key()
wallet_my = k.to_wif()
print('Private key:', k.to_wif())
print('Public address:', k.address)

#k = Key("cQTtf1ZGfJd8k4Jcq4F5UYREYCHdQtwSy6DMyiy4T1iWYGPZ4bGE")##public mwe1UYZXZ48nLnSr1H4TkVjasKVopHgRjc
print(k.get_balance())  # 1391025

#source_k = Key('cQTtf1ZGfJd8k4Jcq4F5UYREYCHdQtwSy6DMyiy4T1iWYGPZ4bGE')
#dest_k = Key('bc1q9jutuqhax5dh2c3k9r60hwdrvstkx893t5zky0')
print(f'Send from {k.address} to {"bc1q9jutuqhax5dh2c3k9r60hwdrvstkx893t5zky0"}')
r = k.send([
    ("bc1q9jutuqhax5dh2c3k9r60hwdrvstkx893t5zky0", 0.01972653, 'btc')
])
print(r)  # ID транзакции

'''