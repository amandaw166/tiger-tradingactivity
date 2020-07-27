import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Define CSV file
EXT870_0706 = "EXT870_2GU_20200706.CSV"
EXT871_0706 = "EXT871_2GU_218076_20200706.CSV"
EXT872_0706 = "EXT872_2GU_218077_20200706.CSV"

# Read in CSV file
df_870 = pd.read_csv(EXT870_0706)
df_871 = pd.read_csv(EXT871_0706)
df_872 = pd.read_csv(EXT872_0706)

# Sort CSV files by columns and contents of columns
df_870_sorted = df_870.loc[
    (df_870["AccountNumber"] == "2GU05001") & (df_870["AccountType"] == "1")
]
df_870_sorted2 = df_870_sorted.loc[
    :, df_870_sorted.columns.isin(["AccountNumber", "AccountType", "Cusip", "Quantity"])
]


df_871_sorted = df_871.loc[
    (df_871["AccountNumber"] == "2GU05001") & (df_871["AccountType"] == "1")
]
# Renamed columns in 871
df_871_sorted2 = df_871_sorted.loc[
    :,
    df_871_sorted.columns.isin(["AccountNumber", "AccountType", "Cusip", "Quantity"]),
]

# Does not account for only AccountType of 1

df_872_sorted = df_872.loc[
    (df_872["AccountNumber"] == "2GU05001") & (df_872["AccountType"] == 1)
]
df_872_sorted2 = df_872_sorted.loc[
    :, df_872_sorted.columns.isin(["AccountNumber", "AccountType", "Cusip", "Quantity"])
]
print (df_871_sorted2)

#df_871_sorted2['Cusip'] = df_872_sorted2['Cusip']

#df_872_sorted2['Final Quantity'] = np.where(df_871_sorted2['Cusip'] == df_872_sorted2['Cusip'], 
#df_871_sorted2['Quantity'] + df_872_sorted2['Quantity'])
#print (df_871_sorted2)

#df_all = pd.concat([df_871_sorted2, df_872_sorted2])
#pivot = df_all.sort_values("Cusip")
#print(pivot)
#df['final'] = 


# print(df_third_shift["AccountNumber"])

# df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
# print(df_all)


# pivot = df_all.groupby(['Shift']).mean()
# shift_productivity = pivot.loc[:,"Production Run Time (Min)":"Products Produced (Units)"]
# loc: choose multiple rows at once, : is every row, and then choose the two columns

# print(shift_productivity)

# #shift_productivity.plot(kind='bar')
# #plt.show()

# df_all.to_excel("output.xlsx")
