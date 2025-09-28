import requests

def get_crypto_price(crypto_id='bitcoin', vs_currency='usd'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={vs_currency}'
    response = requests.get(url)
    data = response.json()
    price = data.get(crypto_id, {}).get(vs_currency)
    if price:
        print(f"{crypto_id.capitalize()} fiyatı: {price} {vs_currency.upper()}")
    else:
        print("Fiyat bilgisi alınamadı.")

if __name__ == "__main__":
    crypto = input("Fiyatını öğrenmek istediğiniz kripto para (ör: bitcoin): ").strip().lower()
    get_crypto_price(crypto)