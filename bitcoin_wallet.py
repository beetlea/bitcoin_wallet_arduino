#https://tirinox.ru/send-bitcoin-over-python/?ysclid=lb1xuaxi9z988165321
from bit import PrivateKey as Key
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Bticoin Wallet")
root.maxsize(1000, 400)
root.minsize(400, 400)
frm = ttk.Frame(root, padding=20)
state = StringVar()
state.set('Не подключенно')

def handle_click():
    global state
    state.set("Подключенно")
    print("Нажата кнопка!")

languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)

frm.grid()
ttk.Label(frm, text="ВВедите пин").grid(column=0, row=0)
ttk.Label(frm, text="Состояние:").grid(column=4, row=0)
ttk.Label(frm, textvariable=state).grid(column=5, row=0)
ttk.Button(frm, text="Подключится", command=handle_click).grid(column=4, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=6)
button = Button(frm, text="Кликни!", command=handle_click).grid(column=0, row=3)
 
listbox1=Listbox(frm,height=5,width=15, listvariable=languages_var, selectmode=EXTENDED).grid(column=2, row=3)

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