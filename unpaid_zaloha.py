# -- coding: utf-8 --
import os
import glob
import pandas as pd
from datetime import datetime

os.chdir("/Plocha/Heureka/inp/")

extension = 'csv'
new_list = []
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

list_of_unpaid_invoices = []
empty_list = []


for file in all_filenames:
                 # headers & podminka

    if os.stat(file).st_size != 0:
        df = pd.read_csv(file,
                         sep=';',
                         names=["Symbols", "Creation", "Date", "Amount", "VAT", "Payment_Type", "IsPayed"],
                         engine='python')

        #ziskat IsPayed hodnoty sloupce
        isPayed = df['IsPayed'][0]
        invoiceDate = df['Date'][0]
        invoiceDate = datetime.strptime(invoiceDate, '%Y-%m-%d %H:%M:%S')
        invoiceDate = invoiceDate.strftime('%Y-%m-%d')
        today = datetime.today().strftime('%Y-%m-%d')

        #pokud je Day dneska
        if invoiceDate == today:
            #if IsPayed equals to 0 append file to list of unpaid invoices
            if isPayed == 0:
                list_of_unpaid_invoices.append(file)
                print(file + " is unpaid and was added to final list")
            else:
                print(file + " is paid")
        else:
            print(file + " is not today")


            #pokud je list s unpaid_invoices prazdny - napise "print()"
if list_of_unpaid_invoices == []:
    print("There are no unpaid invoices for today")
    exit()
else:
    print ("There are " + str(len(list_of_unpaid_invoices)) + " unpaid invoices for today")

combined_csv = pd.concat([pd.read_csv(f) for f in list_of_unpaid_invoices])


write_file = "nezaplacene.csv"
with open(write_file, "wt", encoding="utf-8") as output:
    output.write('Symbols;Creation;Date;Amount;VAT;Payment_Type;IsPayed\n')
    for line in combined_csv:
        output.write(line + '\n')

                  # precte zarovnane sloupce line by line
results = pd.read_csv("nezaplacene.csv")
print(results)
print("\n "">>> ALL IS SAVE IN --> (  nezaplacene.csv  ) FILE")
