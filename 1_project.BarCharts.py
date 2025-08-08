import pandas as pd 
import matplotlib.pyplot  as plt

#LOAD THE DATA

df=pd.read_csv("netflix_titles.csv")

#clean the data

df=df.dropna(subset=['type','release_year','rating','country','duration'])

type_counts=df['type'].value_counts()  #COUNTS ALL THE UNIQUE VALUES IN THE DATA SET
#print(type_counts)
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=["skyblue","lightpink"])
plt.title("movies vs tv shows")
plt.xlabel('type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig("movies vs tv shows.png")
plt.show()
#--------------------------------------------------------------------------

