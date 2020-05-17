# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path,sep=",")
data.rename(columns={"Total":"Total_Medals"},inplace=True)
data.head(10)


# --------------
#Code starts here
data["Better_Event"]=np.where(data['Total_Summer']>data['Total_Winter'],'Summer',(np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter')))
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)
#print(top_countries.tail())

def top_ten(df,col_name):
    country_list=[]
    top=df.nlargest(10, col_name)
    country_list=top['Country_Name']
    return country_list

top_10_summer=list(top_ten(top_countries,'Total_Summer'))
#print(top_10_summer)
top_10_winter=list(top_ten(top_countries,'Total_Winter') )
#print(top_10_winter)
top_10=list(top_ten(top_countries,'Total_Medals'))
#print(top_10)

common=list(set(top_10_summer).intersection(set(top_10_winter).intersection(top_10)))
print(common)


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]


summer_df.plot.bar(x='Country_Name',y='Total_Summer',title="summer")
winter_df.plot.bar(x='Country_Name',y='Total_Winter',title="winter")
top_df.plot.bar(x='Country_Name',y='Total_Medals',title="total")


# --------------
#Code starts here
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
#print(summer_df.head(1))
summer_max_ratio=summer_df["Golden_Ratio"].max()
#print(summer_max_ratio)
summer_country_gold=summer_df.loc[summer_df["Golden_Ratio"].idxmax(),"Country_Name"]
print(summer_country_gold)


winter_df["Golden_Ratio"]=winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max_ratio=winter_df["Golden_Ratio"].max()
winter_country_gold=winter_df.loc[winter_df["Golden_Ratio"].idxmax(),"Country_Name"]
print(winter_country_gold)

top_df["Golden_Ratio"]=top_df["Gold_Total"]/top_df["Total_Medals"]
top_max_ratio=top_df["Golden_Ratio"].max()
top_country_gold=top_df.loc[top_df["Golden_Ratio"].idxmax(),"Country_Name"]
print(top_country_gold)


# --------------
#Code starts here
data_1=data[:-1]
print(type(data_1))

data_1["Total_Points"]=(data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)
print(data_1["Total_Points"].head(10))

most_points=data_1["Total_Points"].max()
print(most_points)

best_country=data_1.loc[data_1["Total_Points"].idxmax(),"Country_Name"]
print(best_country)


# --------------
#Code starts here
best=data[data["Country_Name"]==best_country]
print(type(best))

best=best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best.head())

best.plot.bar(stacked=True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)



