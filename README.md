Let’s have a list of text files. Files contain invoice data, saved in CSV format.

     Variable symbol; Creation date; Due Date; Amount; VAT; Payment type; IsPayed;
     
Write the script (and add to Gitlab) which is able to process these files and create these output files in CSV:
1) List of invoices created last month
2) The total amount of created invoices per month (without VAT and with VAT)
3) Total amount by Payment type
4) Find unpaid invoices for today
5) Measure the script’s performance and find how to optimize it
----
Zkus využít faktu, že už názvy souborů obsahují datum a čas v podobě timestampu
Není Pandas trochu overkill? Co zkusit raději modul csv viz https://www.programiz.com/python-programming/reading-csv-files
