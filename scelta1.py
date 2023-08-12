
import csv
from bs4 import BeautifulSoup
import requests


def scelta1(HEADERS):

            prodotto = input(
                "Inserire il link del prodotto di cui si vuole tenere traccia: ")
            webpage = requests.get(prodotto, headers=HEADERS)
            soup = BeautifulSoup(webpage.text, "html.parser")

            block_div_prezzo = soup.find_all("span", attrs={
                                            "class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
            block_div_title = soup.find_all(
                "div", attrs={"class": "a-section a-spacing-none"})
            block_div_prezzo2 = soup.find_all(
                "span", attrs={"class": "a-size-base a-color-price a-color-price"})

            # cerca il prezzo
            if "a-price-whole" in str(block_div_prezzo):
                for block in range(len(block_div_prezzo)):
                    prezzo_temp = str(block_div_prezzo[block].find("span", attrs={'class': 'a-offscreen'})).replace(
                        "<span class=\"a-offscreen\">", "").replace("</span>", "").replace("€", "").replace(".", "")
                    prezzo_fin = float(prezzo_temp.replace(",", "."))
            elif "a-size-base a-color-price a-color-price" in str(block_div_prezzo2):
                for block in range(len(block_div_prezzo2)):
                    prezzo_temp = str(block_div_prezzo2[block]).replace("<span class=\"a-size-base a-color-price a-color-price\">", "").replace(
                        "</span>", "").replace("€", "").replace(".", "").replace("&nbsp", "")
                    prezzo_fin = float(prezzo_temp.replace(",", "."))
            elif "a-spacing-none a-text-left a-size-mini twisterSwatchPrice" in str(block_div_prezzo2):
                prezzo_temp = str(block_div_prezzo2[block]).replace("<span class=\"a-spacing-none a-text-left a-size-mini twisterSwatchPrice\">", "").replace(
                    "</span>", "").replace("€", "").replace(".", "").replace("&nbsp", "")
                prezzo_fin = float(prezzo_temp.replace(",", "."))
            else:
                print("prezzo non trovato")

                # cerca il nome del prodotto
            for _ in range(len(block_div_title)):
                title = soup.find(
                    "span", attrs={"id": "productTitle"}).text.strip()

            filename = 'products.csv'
            with open(filename, 'a') as csv_file:
                pass  # Nessuna operazione effettuata

            with open(filename, 'r') as csv_file:
                reader = csv.reader(csv_file)
                row_num = sum(1 for _ in reader)
            lista_prodotti = [(f"{str(row_num + 1)})", title, str(prezzo_fin), prodotto)]

            with open("products.csv", "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)

                for product in lista_prodotti:
                    writer.writerow(product)