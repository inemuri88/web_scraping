# sourcery skip: merge-nested-ifs, use-fstring-for-concatenation
from bs4 import BeautifulSoup
import requests

import shutil
import locale
import csv
import winsound

import tempfile
import shutil

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')




while True:    

    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'})

    print("Vuoi vedere la lista di prodotti di cui stai tenendo traccia o vuoi inserire un nuovo prodotto?")

    scelta = int(input("-Per inserire un prodotto premi 1\n-Per visualizzare la lista dei prodotti premi 2\n-Per eliminare un prodotto premi 3: "))



    #inserisco un nuovo prodotto tramite link
    if scelta == 1:
            prodotto = input("Inserire il link del prodotto di cui si vuole tenere traccia: ")
            webpage = requests.get(prodotto, headers=HEADERS)
            soup = BeautifulSoup(webpage.text, "html.parser")

            block_div_prezzo = soup.find_all("span", attrs={"class":"a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
            block_div_title = soup.find_all("div", attrs={"class":"a-section a-spacing-none"})
            block_div_prezzo2 = soup.find_all("span", attrs={"class":"a-size-base a-color-price a-color-price"})


            #cerca il prezzo
            if "a-price-whole" in str(block_div_prezzo):
                for block in range(len(block_div_prezzo)):
                    prezzo_temp = str(block_div_prezzo[block].find("span", attrs={'class':'a-offscreen'})).replace("<span class=\"a-offscreen\">", "").replace("</span>", "").replace("€", "").replace(".", "")
                    prezzo_fin = float(prezzo_temp.replace(",", "."))
            elif "a-size-base a-color-price a-color-price" in str(block_div_prezzo2):
                for block in range(len(block_div_prezzo2)):            
                    prezzo_temp = str(block_div_prezzo2[block]).replace("<span class=\"a-size-base a-color-price a-color-price\">", "").replace("</span>", "").replace("€", "").replace(".", "").replace("&nbsp", "")       
                    prezzo_fin = float(prezzo_temp.replace(",", "."))
            elif "a-spacing-none a-text-left a-size-mini twisterSwatchPrice" in  str(block_div_prezzo2):
                prezzo_temp = str(block_div_prezzo2[block]).replace("<span class=\"a-spacing-none a-text-left a-size-mini twisterSwatchPrice\">", "").replace("</span>", "").replace("€", "").replace(".", "").replace("&nbsp", "")       
                prezzo_fin = float(prezzo_temp.replace(",", "."))
            else:
                print("prezzo non trovato")

                        #cerca il nome del prodotto
            for _ in range(len(block_div_title)):
                    title = soup.find("span", attrs={"id":"productTitle"}).text.strip() 

            filename = 'products.csv'
            with open(filename, 'a') as csv_file:
                pass # Nessuna operazione effettuata

            with open(filename, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    row_num = sum(1 for _ in reader)
            lista_prodotti = [(str(row_num+1)+")",title, str(prezzo_fin), prodotto)]

            with open("products.csv", "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)

                for product in lista_prodotti:
                    writer.writerow(product)



    elif scelta == 2:
            with open("products.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    row_num, product_name, price, link = row
                    print(f"{row_num} Nome prodotto: {product_name}, Prezzo: {price}, Link: {link} \n")
                    prodotto = link
                    webpage = requests.get(prodotto, headers=HEADERS)
                    soup = BeautifulSoup(webpage.text, "html.parser")
                    block_div_prezzo = soup.find_all("span", attrs={"class":"a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
                    block_div_prezzo2 = soup.find_all("span", attrs={"class":"a-size-base a-color-price a-color-price"})

                    if "a-price-whole" in str(block_div_prezzo):
                        for block in range(len(block_div_prezzo)):
                            prezzo_temp2 = str(block_div_prezzo[block].find("span", attrs={'class':'a-offscreen'})).replace("<span class=\"a-offscreen\">", "").replace("</span>", "").replace("€", "").replace(".", "")
                            prezzo_fin2 = float(prezzo_temp2.replace(",", "."))
                    elif "a-size-base a-color-price a-color-price" in str(block_div_prezzo2):
                        for block in range(len(block_div_prezzo2)):            
                            prezzo_temp2 = str(block_div_prezzo2[block]).replace("<span class=\"a-size-base a-color-price a-color-price\">", "").replace("</span>", "").replace("€", "").replace(".", "").replace("&nbsp", "")       
                            prezzo_fin2 = float(prezzo_temp2.replace(",", "."))

                    if prezzo_fin2 < float(price):

                        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                        print(f"Il prezzo del prodotto appena mostrato è minore del prezzo di quando lo hai inserito, ora vale: {prezzo_fin2}\n")

    elif scelta == 3:
            # Definisci il nome del file CSV
            filename = 'products.csv'

            # Definisci l'indice della riga che vuoi rimuovere
            row_index = int(input('Inserire la riga da eliminare: '))

            # Crea un file temporaneo
            temp_file = tempfile.NamedTemporaryFile(mode='w', newline='', delete=False)

            # Apri il file CSV e il file temporaneo
            with open(filename, 'r') as csv_file, temp_file:
                # Crea un oggetto lettore CSV e un oggetto scrittore CSV
                reader = csv.reader(csv_file)
                writer = csv.writer(temp_file)

                # Itera le righe del file di input CSV e scrivi le righe tranne quella che vuoi rimuovere nel file temporaneo
                for i, row in enumerate(reader,start=1):
                    if i != row_index:
                        writer.writerow(row)

            # Sostituisci il file CSV esistente con il file temporaneo
            shutil.move(temp_file.name, filename)



    











    