#downloading Youtube videos


import os
import pandas as pd
import glob
from glob import glob
import ffmpy
import pytube
from pytube import YouTube

com_files=[y for x in os.walk("/playlist/path") for y in glob(os.path.join(x[0], '*.*'))]
d=os.listdir("/Users/skandhvinayak/r2_urls/")
names=[]
for i in d:
    names.append(i.replace(".xlsx",""))


for i in range(len(com_files)):
    s=0
    path="/Volumes/SkAnDH_Xb/final_year_pj/r2/"+names[i]
    os.makedirs(path)
    df=pd.read_excel(com_files[i])
    df.columns=[x.lower() for x in df.columns]
    urls=list(df["video url"])
    not_down=[]
    for url in urls:
        try:
            youtube = pytube.YouTube(url)
            video = youtube.streams.first()
            video.download(path)
            print(s)
            s+=1
        except:
            print("NOT.  :"+str(s))
            not_down.append(url)
            df=df.drop([s])
            s+=1
            continue
    df.to_excel(path+"/"+names[i]+".xlsx")
    with open(path+"/"+names[i]+".txt","w+") as f:
        for t in not_down:
            f.write(t+"\n")
        f.close()