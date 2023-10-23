
import csv
import winsound
from bs4 import BeautifulSoup
import time
import requests

def scelta2(HEADERS):
    with open("products.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    row_num, product_name, price, link = row
                    print(
                        f"{row_num} Nome prodotto: {product_name} \n Prezzo: {price} \n Link: {link} \n")
                    prodotto = link
                    webpage = requests.get(prodotto, headers=HEADERS)
                    soup = BeautifulSoup(webpage.text, "html.parser")
                    block_div_prezzo = soup.find_all("span", attrs={
                                                    "class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
                    block_div_prezzo2 = soup.find_all(
                        "span", attrs={"class": "a-size-base a-color-price a-color-price"})
                    time.sleep(1)
                    if "a-price-whole" in str(block_div_prezzo):
                        for block in range(len(block_div_prezzo)):
                            prezzo_temp2 = str(block_div_prezzo[block].find("span", attrs={'class': 'a-offscreen'})).replace(
                                "<span class=\"a-offscreen\">", "").replace("</span>", "").replace("€", "").replace(".", "")
                            prezzo_fin2 = float(prezzo_temp2.replace(",", "."))
                            if prezzo_fin2 < float(price):

                                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                                print(
                                    f"Il prezzo del prodotto appena mostrato è minore del prezzo di quando lo hai inserito, ora vale: {prezzo_fin2}\n")

                    elif "a-size-base a-color-price a-color-price" in str(block_div_prezzo2):
                        for block in range(len(block_div_prezzo2)):
                            prezzo_temp2 = str(block_div_prezzo2[block]).replace("<span class=\"a-size-base a-color-price a-color-price\">", "").replace(
                                "</span>", "").replace("€", "").replace(".", "").replace("&nbsp", "")
                            prezzo_fin2 = float(prezzo_temp2.replace(",", "."))
                            if prezzo_fin2 < float(price):

                                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                                print(
                                    f"Il prezzo del prodotto appena mostrato è minore del prezzo di quando lo hai inserito, ora vale: {prezzo_fin2}\n")


