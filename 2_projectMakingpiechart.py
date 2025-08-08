import pandas as pd 
import matplotlib.pyplot  as plt

#LOAD THE DATA

df=pd.read_csv("netflix_titles.csv")

#clean the data

df=df.dropna(subset=['type','release_year','rating','country','duration'])

rating_counts=df['rating'].value_counts()
print(rating_counts)
plt.figure(figsize=(6,4))
plt.pie(rating_counts.values, labels=rating_counts.index,autopct='%1.1f%%' )

plt.title("movies rating")
plt.tight_layout()
plt.savefig("moviesrating.png")
plt.show()

