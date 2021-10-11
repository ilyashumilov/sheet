import pandas as pd
import openpyxl
df = pd.read_csv('/Users/ilya.shumilov/Desktop/Sorting/Shipments Update.csv')
df1 = pd.read_csv('/Users/ilya.shumilov/Desktop/Sorting/Новая таблица - Лист1.csv')
countries = ['BELIZE',
'COSTA RICA',
'EL SALVADOR',
'GUATEMALA',
'HONDURAS',
'MEXICO',
'NICARAGUA',
'PANAMA',
'ARGENTINA',
'BOLIVIA',
'BRAZIL',
'CHILE',
'COLOMBIA',
'ECUADOR',
'FRENCH GUIANA',
'GUYANA',
'PARAGUAY',
'PERU',
'SURINAME',
'URUGUAY',
'VENEZUELA',
'CUBA',
'DOMINICAN REPUBLIC',
'HAITI',
'PUERTO RICO']
count = 0
lista = []

for i in df['DESTINATION_COUNTRY']:
    Flag = False
    for n in countries:
        if i == n:
            Flag = True

    if Flag == False:

        lista.append(count)
    count += 1
fin = df.copy()
fin.drop(fin.index[lista], inplace=True)
fin = fin.reset_index(drop=True)
count = 0
lista = []
for i in fin['DESTINATION_COUNTRY']:
    Flag = True
    for n in df1['Document number']:
        if fin.loc[count,'DOCUMENT_NUMBER'] == n:
            Flag = False
    if Flag == False: 
        lista.append(count)
    count += 1
fin.drop(fin.index[lista], inplace=True)
fin = fin.reset_index(drop=True)
fin = fin.drop(['Textbox1','CUSTOMER_NAME','CONTRACT_NUMBER','ITEM','PRICE_TN','ORDERED_TNS','THIRD_REFERENCE','LDS',
               'POL','POD','INVOICING_WEIGHT','NUMBER_OF_LOADINGS','TRANSPORT_NAME','ETS'], axis = 1)
fin.to_excel('/Users/ilya.shumilov/Desktop/Sorting/Fin.xlsx')