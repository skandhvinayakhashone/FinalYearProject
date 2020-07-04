import os
import glob
from glob import glob
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import enchant
d = enchant.Dict("en_US")

path="/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/"
dirs_names=os.listdir("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_mp4/")

for p in dirs_names:
    vs=os.listdir("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_avi/"+p+"/t")
    vids=[]
    for v in vs:
        if ".avi" in v:
            n=v.replace(".avi","")
            vids.append(n)
    df=pd.read_excel("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_mp4/"+p+"/"+p+".xlsx",index_col=False)
    name_list=list(df["title"])
    desc_list=list(df["description"])
    desc_=[]
    for v in vids:
        for name in range(len(name_list)):
            if fuzz.ratio(v ,name_list[name])>90:
                spi=str(desc_list[name]).replace("\n"," ")
                spi=spi.replace("—"," ")
                spi=spi.replace("-"," ")
                spi=spi.replace("\t"," ")
                spi=spi.replace("—"," ")
                spi_list=spi.split(" ")
                with open("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_all_data/"+p+"/"+str(vids.index(v))+"_desc.txt","w") as f:
                    for sp in spi_list:
                        if sp!="" and sp!=" ":
                            if d.check(sp):
                                f.write(sp+"\n")


def combine(t1,t3,t4=0,t2=0):
    data = data2 = data3 ="" 
  
    # Reading data from file1 
    with open(t1) as fp: 
        data = fp.read() 
    # Reading data from file2 
    if t2:
        with open(t2) as fp: 
            data2 = fp.read() 
    if t4:
        with open(t4) as fp: 
            data3 =fp.read()
            print(data)
    # Merging 2 files 
    # To add the data of file2 
    # from next line 
    data += "\n"
    data += data2 + "\n"
    data += data3 + "\n"
    
    with open (t3, 'w') as fp: 
        fp.write(data) 


for p in dirs_names:
    print(p)
    try:
        new_names=[]
        vd=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_all_data/"+p+"/") for y in glob(os.path.join(x[0], '*.txt'))]
        for i in vd:
            s=i.replace("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_all_data/"+p+"/","")
            s=s.replace("_audio_to_txt.txt","")
            s=s.replace("_desc.txt","")
            s=s.replace("_objects.txt","")
            s=s.replace("_text.txt","")
            s=s.replace("_v1.txt","")
            s=s.replace("_v2.txt","")
            s=s.replace("_v3.txt","")
            s=s.replace("_v4.txt","")
            s=s.replace("_v5.txt","")
            s=s.replace("_v6.txt","")
            s=s.replace("_v7.txt","")
            new_names.append(s)
        set_data=list(set(new_names))
        #print(set_data)
        for n in set_data:
            #V1
            combine("/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_desc.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_v1.txt")
            #V2
            combine("/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_desc.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_v2.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_text.txt")
            #V3
            combine("/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_desc.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_v3.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_audio_to_txt.txt")
            #V4
            combine("/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_desc.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_v4.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_objects.txt")
            #V5
            combine("/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_desc.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_v5.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_text.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_audio_to_txt.txt")
            #V6
            combine("/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_desc.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_v6.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_text.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_objects.txt")
            #V7
            combine("/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_desc.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_v7.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_audio_to_txt.txt","/Volumes/SkAnDH_Xb/final_year_pj/R2_ads/r2_all_data/"+p+"/"+n+"_objects.txt")
    except :
        print(str(p)+str("  "+n))

