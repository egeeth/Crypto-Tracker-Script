import requests

def get_price(coin, currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={{coin}}&vs_currencies={{currency}}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(coin, {}).get(currency, 0)
    else:
        return 0

def main():
    print("Kripto Para Portföy Değer Hesaplayıcı")
    print("Örnek coin isimleri: bitcoin, ethereum, solana, avalanche-2")
    portfolio = {}
    while True:
        coin = input("Coin ismi (bitir için boş bırak): ").strip().lower()
        if not coin:
            break
        try:
            amount = float(input(f"{{coin}} miktarını giriniz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue
        portfolio[coin] = amount

    total = 0
    print("\nPortföyünüz:")
    for coin, amount in portfolio.items():
        price = get_price(coin)
        value = price * amount
        print(f"{{coin.capitalize()}}: {{amount}} x {{price}} USD = {{value:.2f}} USD")
        total += value
    print(f"\nToplam Portföy Değeri: {{total:.2f}} USD")

if __name__ == "__main__":
    main()