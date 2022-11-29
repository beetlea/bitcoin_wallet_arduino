#https://tirinox.ru/send-bitcoin-over-python/?ysclid=lb1xuaxi9z988165321
from bit import PrivateKeyTestnet as Key
k = Key()
wallet_my = k.to_wif()
print('Private key:', k.to_wif())
print('Public address:', k.address)


k = Key(wallet_my)
print(k.get_balance())  # 1391025