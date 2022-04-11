import pandas as pd

#--------------------------------------------------------------------------
#Remove psp, split the "Merchant Reference"

excel_workbook = input(" ENTER the name of Adyen File: ")
shet = pd.read_csv(excel_workbook)
shet1=shet.drop(['PSP Reference', 'TimeZone', 'Currency', 'Risk Score'], axis = 1)

#remove Registration from Account colummn
shet1 = shet1[shet1['Account'].str.contains('Registration') == False]
#print(shet1)
option = input(" ENTER MARKET ID Like IT,MY,CY: ")
#Keep only one market to be compared
shet1 = shet1[shet1['Account'].str.contains(option) == True]


#split reference
shet1.dropna(inplace = True)
new = shet1["Merchant Reference"].str.split("|", n = 1, expand = True)
shet1["Checkin Code"]= new[0]
shet1["Order ID"]= new[1]
shet1.drop(columns =["Merchant Reference"], inplace = True)
#print(shet1)


#export dataframe to csv again
df = pd.DataFrame(shet1)
output=df.rename(columns={"Checkin Code":"CheckInCode"})
output['Value']=100*output['Value']
#output['OrderId'].str.upper()
#print(df)
output.to_csv('output/Adyen_output.csv', index = False)
#====================================================================================================
# clening Database file
excel_workbook1 = input(" ENTER the name of database File: ")
db = pd.read_csv(excel_workbook1)
df1=pd.DataFrame(db)
df1.dropna(axis=1, how="any", thresh=None, subset=None, inplace=True)

#to delete unessary colums
df1.drop(['CurrentStateID','TotalNetPrice','IsPaidOrder','MustBePrinted','TotalTaxWithFee','TotalDiscount','DiscountID',
'TotalBD','OrderTypeFlag','PaymentStatus','SendOrderToFOEStatus','DisplayOrderID','FCkCurrentStateID','OrderSeqId',
'PaymentKeyCounter','ExternalCustomerId','ExternalID','NewTime','ExpirationTime','LastModification'], axis = 1, inplace=True, errors='ignore')
#print(df1)


# change OrderID column name in db file
df1.to_csv('output/database_output.csv', index = False)
#===========================================================================================
#comparing


