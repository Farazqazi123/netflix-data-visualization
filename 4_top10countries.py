import pandas as pd 
import matplotlib.pyplot  as plt

#LOAD THE DATA

df=pd.read_csv("netflix_titles.csv")

#clean the data

df=df.dropna(subset=['type','release_year','rating','country','duration'])

countries_count=df['country'].value_counts().head(10)

plt.barh(countries_count.index,countries_count.values, color='skyblue')

plt.xlabel("num of movies")
plt.ylabel("coountry")
plt.title("Top 10 countries")
plt.tight_layout()

plt.savefig("top 10 countries in movies.png")
plt.show()

