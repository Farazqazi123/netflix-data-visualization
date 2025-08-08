import pandas as pd 
import matplotlib.pyplot  as plt

#LOAD THE DATA

df=pd.read_csv("netflix_titles.csv")

#clean the data

df=df.dropna(subset=['type','release_year','rating','country','duration'])

#getting only movie from whole dataframe
movie_df=df[df['type']=='Movie'].copy()

movie_df["duration_int"]= movie_df['duration'].str.replace('min', ' ').astype(int)

plt.figure(figsize=(9,6))
plt.hist(movie_df['duration_int'],bins=30, color='purple', edgecolor='black')

plt.xlabel("movies duration")
plt.ylabel("hours")
plt.tight_layout()
plt.savefig('movies_duarationhistogram.png')

plt.show()