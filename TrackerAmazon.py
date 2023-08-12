# sourcery skip: merge-nested-ifs, use-fstring-for-concatenation
# from bs4 import BeautifulSoup
# import requests
# import shutil
import locale
import csv
# import winsound
# import tempfile
import shutil
import scelta1
import scelta2
import scelta3
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


while True:

    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'})

    print("Vuoi vedere la lista di prodotti di cui stai tenendo traccia o vuoi inserire un nuovo prodotto?")

    scelta = int(input(
        "-Per inserire un prodotto premi 1\n-Per visualizzare la lista dei prodotti premi 2\n-Per eliminare un prodotto premi 3: "))

    
    if scelta == 1:
        scelta1.scelta1(HEADERS)

    elif scelta == 2:
        scelta2.scelta2(HEADERS)
    elif scelta == 3:
        scelta3.scelta3()

    else:
        print("Scelta sbagliata, uscita dal programma")
        break
