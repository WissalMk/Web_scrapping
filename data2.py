import csv
from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
tbody = doc.tbody
trs = tbody.contents

prices = []

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices.append([fixed_name, fixed_price])

# Écrire les données dans un fichier CSV
csv_file_path = "crypto_prices1.csv"
header = ["Crypto", "Price"]

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(prices)

print("Les données ont été enregistrées dans", csv_file_path)


