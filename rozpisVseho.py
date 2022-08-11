# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd
import io
import csv

#set working directory
from pandas import DataFrame

os.chdir("/home/darskki/Plocha/Heureka/inp1/")

#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
extension = 'csv'
new_list = []
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# colnames = ["Symbols", "Creation", "Date", "Amount", "VAT", "Payment Type", "IsPayed"]

# 1) List of invoices created last month (seznam faktur za minulý měsíc)
list_of_invoices = []
# 2) The total amount of created invoices per month (without VAT and with VAT) (DPH)
list_of_total_amountVAT = []
# 3) Total amount by Payment type (typ platby podle částek)S
list_of_payment = []
# 4) Find unpaid invoices for today (nezaplacené faktury)
list_of_unpaid_invoices = []
# 5) Measure the script’s performance and find how to optimize it (změřit výkon + optimalizovat)
list_of_measure = []

empty_list = []


# Import libraries

# Get CSV files list from a folder
# path = '/home/darskki/Plocha/Heureka/inp1/'
# csv_files = glob.glob(path + "/*.csv")

# print("before read_csv")
# df = pd.read_csv('/home/darskki/Plocha/Heureka/inp1/1640998320.csv',
#                  sep=';',
#                  names=["Symbols", "Creation", "Date", "Amount", "VAT", "Payment_Type", "IsPayed"],
#                  header=None)
#
#
# print("after read_csv")
# print(df)

# for file in os.listdir("/home/darskki/Plocha/Heureka/inp1/"):
#     if file.endswith(".csv"):
#         data_all = pd.concat((pd.read_csv(i) for i in file)).reset_index(drop=True)  # Import
#         print(data_all)

        # header_list = ["Symbols", "Creation", "Date", "Amount", "VAT", "Payment_Type", "IsPayed"]
        # df = pd.read_csv(file, names=header_list)
        # print(df)
        # df = pd.read_csv(file)
        # df = df.reset_index() # this is option line
        # df.columns = ["Symbols", "Creation", "Date", "Amount", "VAT", "Payment_Type", "IsPayed"]
        # df.to_csv(file)

for file in all_filenames:
    # hlavicky + jak dat prazdne misto pryc
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            if len(row) == 0:
                continue

        print("hovno")


        # empty_list.append(df)
        # df = pd.read_csv(file, index_col=None)
        # empty_list.append(df.columns)
        # dfa = pd.DataFrame(df)
#     elif os.stat(file).st_size != 0:
#         df = pd.read_csv(file, index_col=None)
#         list_of_invoices.append(df)
    # elif
    #     list_of_total_amount.append(df.columns)
    # elif


# frame = pd.DataFrame(new_list)

# frame.columns = ["Symbols", "Creation", "Date", "Amount", "VAT", "Payment Type", "IsPayed"]
# frame
# result = [ele for ele in new_list if ele !=[]]
# print(result)

#combiprint(new_list)
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

#export to csv
# combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

# print(combined_csv)
#combine all files in the list
# combined_csv = pd.concat(
#     [pd.read_csv(io.StringIO(f) , skip_blank_lines=True) for f in all_filenames]
# )
# if len(combined_csv)>0:
#     print(combined_csv, "AA")


