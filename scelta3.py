

# Definisci il nome del file CSV
import csv
import shutil
import tempfile

def scelta3():
    filename = 'products.csv'

    # Definisci l'indice della riga che vuoi rimuovere
    row_index = int(input('Inserire la riga da eliminare: '))

    # Crea un file temporaneo
    temp_file = tempfile.NamedTemporaryFile(
        mode='w', newline='', delete=False)

    # Apri il file CSV e il file temporaneo
    with open(filename, 'r') as csv_file, temp_file:
        # Crea un oggetto lettore CSV e un oggetto scrittore CSV
        reader = csv.reader(csv_file)
        writer = csv.writer(temp_file)

        # Itera le righe del file di input CSV e scrivi le righe tranne quella che vuoi rimuovere nel file temporaneo
        for i, row in enumerate(reader, start=1):
            if i != row_index:
                writer.writerow(row)

    # Sostituisci il file CSV esistente con il file temporaneo
    shutil.move(temp_file.name, filename)