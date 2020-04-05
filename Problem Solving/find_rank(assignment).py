import pandas as pd
from pandas import ExcelWriter
df=pd.read_csv("C:\\Users\Biranchi Padhi\Desktop\soc_net\\rank.csv")
df.head()


df.sort_values(['DC'+"'"],ascending=False,inplace=True)
writer=pd.ExcelWriter('C:\\Users\Biranchi Padhi\Desktop\soc_net\Rank_DC.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()

df.sort_values(['CC'+"'"],ascending=False,inplace=True)
writer=pd.ExcelWriter('C:\\Users\Biranchi Padhi\Desktop\soc_net\Rank_CC.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()

df.sort_values(['BC'+"'"],ascending=False,inplace=True)
writer=pd.ExcelWriter('C:\\Users\Biranchi Padhi\Desktop\soc_net\Rank_BC.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
