# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd

os.chdir("/home/darskki/Plocha/Heureka/inp1/")


extension = 'csv'
new_list = []
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# colnames = ["Symbols", "Creation", "Date", "Amount", "VAT", "Payment Type", "IsPayed"]

list_of_total_amountVAT = []
empty_list = []


for file in all_filenames:
                 # headers & podminka

    if os.stat(file).st_size != 0:
        df = pd.read_csv(file,
                         sep=';',
                         names=["Symbols", "Creation", "Date", "Amount", "VAT", "Payment_Type", "IsPayed"],
                         )
        # print(df) ##  >> precte jednotlive vsechny csv


combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])


write_file = "List_of_Invoices5.csv"
with open(write_file, "wt", encoding="utf-8") as output:
    for line in combined_csv:
        output.write(line + '\n')

                  # precte zarovnane sloupce line by line
results = pd.read_csv("List_of_Invoices5.csv")
print(results)
print("\n "">>> ALL IS SAVE IN --> (  List_of_Invoices  ) FILE")