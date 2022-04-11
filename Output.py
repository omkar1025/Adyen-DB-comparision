import pandas as pd

data1 = pd.read_csv('output/Adyen_output.csv')
data2 = pd.read_csv('output/database_output.csv')
output1 = pd.merge(data1, data2,on='CheckInCode', how='right',indicator=True)
print(output1)
output1.drop_duplicates(subset ="CheckInCode",keep = False, inplace = True)
output1.to_csv('output/final.csv')