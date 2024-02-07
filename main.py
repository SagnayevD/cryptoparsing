import requests
from bs4 import BeautifulSoup


d1 = []
d1 = {}
headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest"
    }
url = "https://coinmarketcap.com/"
response = requests.get(url,headers = headers)
soup = BeautifulSoup(response.text, "lxml")
name = soup.find_all("p",class_="sc-4984dd93-0 kKpPOn")
price = soup.find_all("div", class_="sc-a0353bbc-0 gDrtaY")
for i in range(0,len(name)):
    # print(f"{name[i].text} : {price[i].text}")
    a = float(price[i].text.replace("$", "").replace(",",""))
    for d in name:
        b = str(name[i].text)
        # d1[name[i].text] = a
        d1[b.upper()] = a

d1= sorted(d1.items(), key=lambda item: item[1])
d1.sort()
print(f"{d1}\n")



url = "https://cryptoprices.com/wp-admin/admin-ajax.php?draw=1&colrankumns%5B0%5D%5Bdata%5D=rank&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=name&columns%5B1%5D%5Bname%5D=name&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=price_usd&columns%5B2%5D%5Bname%5D=price_usd&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=percent_change_1h&columns%5B3%5D%5Bname%5D=percent_change_1h&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=percent_change_24h&columns%5B4%5D%5Bname%5D=percent_change_24h&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=percent_change_7d&columns%5B5%5D%5Bname%5D=percent_change_7d&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=percent_change_30d&columns%5B6%5D%5Bname%5D=percent_change_30d&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=volume_usd_24h&columns%5B7%5D%5Bname%5D=volume_usd_24h&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=market_cap_usd&columns%5B8%5D%5Bname%5D=market_cap_usd&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=actions&columns%5B9%5D%5Bname%5D=actions&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=false&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false&action=coinmc_table&id=18&watchlist=false&restrict=false&currency=USD&_=1694702446672"

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest"
    }

d2=[]
d2 = {}
count = 0
result = requests.get(url,headers= headers).json()
for coin in result["data"]:
    count += 1
    name_soup = BeautifulSoup(coin["name"], "lxml")
    price_soup = BeautifulSoup(coin["price_usd"],"lxml")
    name_coin = name_soup.find("img").get("alt")
    price_coin = price_soup.find_all("span")[-1].text
                # print(f"\nName: {name_coin}\nPrice: {price_coin}\n")
    a = float(price_coin.replace(",",""))
    d2[name_coin.upper()] = a
    if count >= 10:
        break

                  
d2 = sorted(d2.items(), key=lambda item: item[1])
# sorted = sorted(d2.items(), key=lambda item: item[1], reverse=True)
d2.sort()
print(f"\n{d2}")

with open("Crypto.txt", "w") as cr:
    cr.write(f"Bitcoin:\n\tCryptoprices: {d2[0]}\n\tCoinmarket: {d1[0]} " + "\n")
    cr.write(f"Ethereum:\n\tCryptoprices: {d2[1]}\n\tCoinmarket: {d1[1]}"+"\n")
    cr.write(f"Tether:\n\tCryptoprices: {d2[2]}\n\tCoinmarket: {d1[2]}\n")
    cr.write(f"BNB:\n\tCryptoprices: {d2[3]}\n\tCoinmarket: {d1[3]}\n")
    cr.write(f"XRP:\n\tCryptoprices: {d2[4]}\n\tCoinmarket: {d1[4]}\n")
    cr.write(f"USD Coin:\n\tCryptoprices: {d2[5]}\n\tCoinmarket: {d1[5]}\n")
    cr.write(f"Cardano:\n\tCryptoprices: {d2[6]}\n\tCoinmarket: {d1[6]}\n")
    cr.write(f"Dogecoin:\n\tCryptoprices: {d2[7]}\n\tCoinmarket: {d1[7]}\n")
    cr.write(f"Toncoin:\n\tCryptoprices: {d2[8]}\n\tCoinmarket: {d1[8]}\n")
    cr.write(f"Solana:\n\tCryptoprices: {d2[9]}\n\tCoinmarket: {d1[9]}\n")





