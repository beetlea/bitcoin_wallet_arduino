#https://tirinox.ru/send-bitcoin-over-python/?ysclid=lb1xuaxi9z988165321
from bit import PrivateKeyTestnet as Key

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