import glob
import pandas as pd

lis=glob.glob("C:/Users/ABCD/Videos/Hindi_Lyrics/Bollyrics-master/yearwise_dataset/*/*.txt")

list_of_songs=[]
for i in lis:
    f=open(i,"r")
    list_of_songs.append(str(f.read()))
    f.close()

data=pd.DataFrame(list_of_songs,columns=['Lyrics'])
data.to_csv("Hindi_Songs_DS.csv")
