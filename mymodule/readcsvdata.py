import pandas as pd

#df=pd.read_csv(filepath_or_buffer="C://mydataset//tips.csv", ,usecols=['total_bill','tip'])
# df=pd.read_csv(filepath_or_buffer="C://mydataset//tips.csv",skiprows=10)
# print(df.memory_usage())
df=pd.read_csv(filepath_or_buffer="C://mydataset//tips.csv")
# print(df.shape)
# print(df.info())
#print(df[:15])
# sunday_cust=df.loc[df['day']=='Sun']
# print(sunday_cust.describe())
# male_tips=df.loc[df['sex']=='Male']
# print(male_tips.describe())
# female_tips=df.loc[df['sex']=='Female']
# print(female_tips.describe())
# count=df.groupby(['sex','day']).sum()
 #smokes_no_smokers=df['smoker'].value_counts(normalize=True)
# print(smokes_no_smokers)
# smokers_no_smokers=df.groupby(['sex'])['smoker'].value_counts()
#print(smokers_no_smokers)
df['mes']=df['size'].apply(lambda x:"Large" if x>=3 else "Small")
print(df)