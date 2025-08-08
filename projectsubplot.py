import pandas as pd 
import matplotlib.pyplot  as plt

#LOAD THE DATA

df=pd.read_csv("netflix_titles.csv")

#clean the data

df=df.dropna(subset=['type','release_year','rating','country','duration'])

contentYear=df.groupby(['release_year','type']).size().unstack().fillna(0)
print(contentYear)

fig , ax =plt.subplots(1,2 ,figsize=(12 ,8))

ax[0].plot(contentYear.index , contentYear['Movie'],)
ax[0].set_title("movies released")
ax[0].set_xlabel("year")
ax[0].set_ylabel("movies released")

ax[1].plot(contentYear.index , contentYear['TV Show'],color='red')
ax[1].set_title("shows  released")
ax[1].set_xlabel("year")
ax[1].set_ylabel("shows  released")

plt.tight_layout()
plt.show()

