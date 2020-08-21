import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import warnings

# Define CSV files, replace as needed
EXT870_dayone = "EXT870_2GU_20200706.CSV"
EXT871_dayone = "EXT871_2GU_218076_20200706.CSV"
EXT872_dayone = "EXT872_2GU_218077_20200706.CSV"

EXT870_daytwo = "EXT870_2GU_20200707.CSV"
EXT871_daytwo = "EXT871_2GU_218076_20200707.CSV"
EXT872_daytwo = "EXT872_2GU_218077_20200707.CSV"


# Read in CSV file from each date, replace as needed
df_870_dayone = pd.read_csv(EXT870_dayone)
df_871_dayone = pd.read_csv(EXT871_dayone)
df_872_dayone = pd.read_csv(EXT872_dayone)

df_870_daytwo = pd.read_csv(EXT870_dayone)
df_871_daytwo = pd.read_csv(EXT871_dayone)
df_872_daytwo = pd.read_csv(EXT872_dayone)

# Organize EXT files based on AccountNumber, Account Type, Cusip, Quantity
# Logic of prediction position = EXT871 of DayOne + EXT 870 of DayTwo + EXT 872 of Day Two  
# Example: EXT871 of 7/6/2020 + EXT 870 of 7/7/2020 + EXT 872 of 7/7/2020 
df1 = df_870_daytwo[['AccountNumber', 'AccountType', 'Cusip', 'Quantity']].groupby(['AccountNumber', 'AccountType', 'Cusip']).sum().reset_index()
df2 = df_871_dayone[['AccountNumber', 'AccountType', 'Cusip', 'Quantity']].groupby(['AccountNumber', 'AccountType', 'Cusip']).sum().reset_index()
df3 = df_872_daytwo[['AccountNumber', 'AccountType', 'Cusip', 'Quantity']].groupby(['AccountNumber', 'AccountType', 'Cusip']).sum().reset_index()

df3['AccountType'] = df3['AccountType'].astype('str')

#Merge 870 and 871 files and add the Quantity columns
#IT Suggestion:
#df_1_2 = pd.merge(df1, df2, on = ['AccountNumber', 'AccountType', 'Cusip'], how ='outer')
df_1_2 = pd.merge(df1, df2, on = ['AccountNumber', 'AccountType', 'Cusip'])
df_1_2['Quantity'] = df_1_2['Quantity_x'] + df_1_2['Quantity_y']
df_1_2 = df_1_2.drop(columns = ['Quantity_x', 'Quantity_y'])

#Merge the 872 file, also add the Quantity column
#IT Suggestion:
#df_all = pd.merge(df_1_2, df3, on = ['AccountNumber', 'AccountType', 'Cusip'], how ='outer')
df_all = pd.merge(df_1_2, df3, on = ['AccountNumber', 'AccountType', 'Cusip'])
df_all['Quantity'] = df_all['Quantity_x'] + df_all['Quantity_y']
df_all = df_all.drop(columns = ['Quantity_x', 'Quantity_y'])

#print the dataframe with the prediction
print("Listed are the predictions of the second day based on sum of the EXT871 of the first day, EXT870 of the second day, and the EXT 872 of the second day. Entries are organized by the same AccountNumber, AccountType, and Cusip." )
print(df_all)