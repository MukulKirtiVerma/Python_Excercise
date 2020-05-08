
import pandas as pd
import numpy as np

#read excel file===============================================
df = pd.read_excel(r"D:\tut\ExcelTestData1.xlsx")
#display only first 5 rows=====================================
df.head()
#display first 10 rows=========================================
df.head(10)
#display last 5 rows===========================================
df.tail()

#Assign a value in row column==================================
df.loc[0:1,'MD']=np.nan
print(df)
#replace nan to zero in dataframe=============================
df=df.fillna(0)
#replace set of values with other set of valus================
df2=df.replace([0,2], [5,6])
#replace a range
df.replace(list(range(0,1000)), 0)
#replace set of value with  dectionary==========================
df.replace({0: 10, 2: 100})
df.replace({'MD': 0, 'DT1': 66}, 100)
df.replace({'MD': {0: 100, 4: 400}})
#replace with condition========================================
df[df<=2]=1

#list all column name==========================================
print(list(df.columns))
#list all index================================================
print(list(df.index))

r=list(df.index)
c=list(df.columns)
#iterate dataframe ============================================
for i in df.index:
    x=list(df.loc[i][:])
    print(x)

#adding new column having sum of other columns=================
df["total"] = df["MD"] + df["DT1"] + df["RHOB1"]
df.head()

#some functions================================================
df["MD"].sum(), #sum ofMD column
df["MD"].mean(),
df["MD"].min(),
df["MD"].max()

df[["MD","DT1"]].max()#return seriese with max of both columns

#add row having sum of DT1 and RHOB1 column====================
sum_row=df[["DT1","RHOB1"]].sum()
sum_row

df_sum=pd.DataFrame(data=sum_row).T
df_sum

df_sum=df_sum.reindex(columns=df.columns)
df_sum


df_final=df.append(df_sum,ignore_index=True)
df_final.tail()


#inserting a col in particular position
df_final.insert(4, "abb",2)
df_final.insert(4, "abb22", np.nan)
df_final.insert(4, "abb1", df['MD'])
df_final.insert(4, "abb2", "hi")
df_final.head()

#some grouping example
ddd=df.sort_values(by=['DT1'])
ddd=df.groupby(['DT1']).count()
ddd=df.groupby(['DT1']).first()
ddd=df.groupby(['DT1']).max()
ddd=df.groupby(['DT1']).min()

df_sub=df[["MD","RHOB1","DT1"]].groupby('DT1').sum()
df_sub

#writing dataframe to excel file with diffent sheet
writer = pd.ExcelWriter(r'D:\tut\output.xlsx')
ddd.to_excel(writer,'Sheet1')
df_final.to_excel(writer,'Sheet2')
writer.save()

#parsing diffrent sheet of excel file
xl = pd.ExcelFile(r"D:\tut\output.xlsx")
xl2=xl.sheet_names
df = xl.parse("Sheet1")
df.head()


subham = pd.read_excel(r"D:\tut\output.xlsx",sheetname='Sheet2')
df
dframe = pd.read_excel(r"D:\tut\output.xlsx", sheetname='Sheet1')
df
df = pd.read_excel(r"D:\tut\output.xlsx",sheetname=1)

df= pd.read_excel(r"D:\tut\output.xlsx",sheetname=1,header=None)

dframe = pd.read_excel(r"D:\tut\output.xlsx", sheetname=1,header=1)
dframe1 = pd.read_excel(r"D:\tut\output.xlsx", sheetname=1)

dframe = pd.read_excel(r"D:\tut\output.xlsx",sheetname=1, index_col=2)

dframe = pd.read
dframe = pd.read_excel(r"D:\tut\output.xlsx",sheetname=1, skiprows=2)

df=pd.read_excel(r"D:\tut\output.xlsx", sheetname=1,skip_footer=2)
dframe = pd.read_excel(r"D:\tut\output.xlsx", skip_footer=2)
dframe = pd.read_excel(r"D:\tut\output.xlsx", sheetname=1, skiprows=2,skip_footer=2)
print(str(list(df)))
for i in list(df.index):
    for j in list(df):
      print(df.loc[i,j],end="       ")
    print()
for i in df['MD']:
    print(i)




