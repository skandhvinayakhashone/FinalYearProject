import os
import pandas as pd
import glob
from glob import glob
from statistics import mean

#importing recommendation engines

import rec_v1
import rec_v2
import rec_v3
import rec_v4
import rec_v5
import rec_v6
import rec_v7



#v1=recommendation engine using the description of user history
#v2=recommendation engine using the description of user history and texts in the video frames
#v3=recommendation engine using the description of user history and audio data of the video
#v4=recommendation engine using the description of user history and objects present in the video
#v5=recommendation engine using the description of user history and texts and audio in the video
#v6=recommendation engine with the description of user history and texts and objects in the video 
#v7=recommendation engine with the description of user history and audio data and objects in the video


print(" -------------------------------------------")
print("|                                           |")
print("|      SKANDH RECOMMENDATION ENGINE V2      |")
print("|                                           |")
print(" ------------------------------------------- ")
print("\n")

ratings=[]
for r in range(0,7):
    ratings.append([])

repeat="y"

while repeat=="y":
    dirs=os.listdir("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_avi/")
    test_v=[]
    for d in dirs:
        test_=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_avi/"+d+"/") for y in glob(os.path.join(x[0], '*.avi'))]
        test_v.append(test_)
    test_vids=[j for i in test_v for j in i]
    print("Please choose the videos you wish to watch from the list below")
    print("\n")
    print("type \"end\" to finish")
    print("\n")
    inp=0
    vi=[]
    for v in test_vids:
        print(str(test_vids.index(v))+". "+v.replace("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_avi/",""))

    print("\n\n")
    while inp!="end":
        inp=input()
        if inp!="end":
            try:
                if int(inp)>=0 and int(inp)<=len(test_vids)-1:
                    vi.append(test_vids[int(inp)].replace("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_avi/",""))
                else:
                    print("please ender a valid input\n")
            except:
                print("please enter a valid integer\n")
        elif inp=="end":
            break
    vi=vi[:len(vi)]
    vids=vi.copy()
    
    print(vids)
    yolo_input=[]
    for i in vids:
    	yolo_input.append("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_avi/"+i)
    
    #Generating datasets

    for i in yolo_input:
    	os.system("python /Volumes/SkAnDH_Xb/final_year_pj/R2_/detect_video_objects.py --video "+i)
    	os.system("python /Volumes/SkAnDH_Xb/final_year_pj/R2_/audio_to_text.py "+i)
    	os.system("python /Volumes/SkAnDH_Xb/final_year_pj/R2_/video_to_text.py "+i)

    '''for v in vi:
        vids.append(test_vids[v])
    '''
    
    print('There will be 7 advertisements recommended to you. Please rate the videos recommended, on a scale of 1 - 5 after the advertisement is played. Press enter/return to proceed.')

    ok=1
    while ok==1:
        ok=input()

    df_list_v1=[]
    df_list_v2=[]
    df_list_v3=[]
    df_list_v4=[]
    df_list_v5=[]
    df_list_v6=[]
    df_list_v7=[]


    for v in vids:
        n=v.replace(".avi","_v1.txt")
        df_list_v1.append(n)
        n=v.replace(".avi","_v2.txt")
        df_list_v2.append(n)
        n=v.replace(".avi","_v3.txt")
        df_list_v3.append(n)
        n=v.replace(".avi","_v4.txt")
        df_list_v4.append(n)
        n=v.replace(".avi","_v5.txt")
        df_list_v5.append(n)
        n=v.replace(".avi","_v6.txt")
        df_list_v6.append(n)
        n=v.replace(".avi","_v7.txt")
        df_list_v7.append(n)
      
    #V1
    print("Playing Advertisement using Recommendation V1\n")
    vid_to_play=rec_v1.recommend(df_list_v1)
    os.system("/Applications/VLC.app/Contents/MacOS/VLC "+str(vid_to_play))
    rate=0
    while True:
        try:
            rate=int(input("please enter a rating between 1 and 5    "))
            if rate>0 and rate<6:
                break
            else:
                print("please enter value between 1 and 5")
        except:
            print("please enter a valid integer")
    ratings[0].append(rate)

    #V2
    print("Playing Advertisement using Recommendation V2\n")
    vid_to_play=rec_v2.recommend(df_list_v2)
    os.system("/Applications/VLC.app/Contents/MacOS/VLC "+str(vid_to_play))
    rate=0
    while True:
        try:
            rate=int(input("please enter a rating between 1 and 5    "))
            if rate>0 and rate<6:
                break
            else:
                print("please enter value between 1 and 5")
        except:
            print("please enter a valid integer")
    ratings[1].append(rate)
    
    #V3
    print("Playing Advertisement using Recommendation V3\n")
    vid_to_play=rec_v3.recommend(df_list_v3)
    os.system("/Applications/VLC.app/Contents/MacOS/VLC "+str(vid_to_play))
    rate=0
    while True:
        try:
            rate=int(input("please enter a rating between 1 and 5    "))
            if rate>0 and rate<6:
                break
            else:
                print("please enter value between 1 and 5")
        except:
            print("please enter a valid integer")
    ratings[2].append(rate)
    
    #V4
    print("Playing Advertisement using Recommendation V4\n")
    vid_to_play=rec_v4.recommend(df_list_v4)
    os.system("/Applications/VLC.app/Contents/MacOS/VLC "+str(vid_to_play))
    rate=0
    while True:
        try:
            rate=int(input("please enter a rating between 1 and 5    "))
            if rate>0 and rate<6:
                break
            else:
                print("please enter value between 1 and 5")
        except:
            print("please enter a valid integer")
    ratings[3].append(rate)
    
    #V5
    print("Playing Advertisement using Recommendation V5\n")
    vid_to_play=rec_v5.recommend(df_list_v5)
    os.system("/Applications/VLC.app/Contents/MacOS/VLC "+str(vid_to_play))
    rate=0
    while True:
        try:
            rate=int(input("please enter a rating between 1 and 5    "))
            if rate>0 and rate<6:
                break
            else:
                print("please enter value between 1 and 5")
        except:
            print("please enter a valid integer")
    ratings[4].append(rate)
    
    #V6
    print("Playing Advertisement using Recommendation V6\n")
    vid_to_play=rec_v6.recommend(df_list_v6)
    os.system("/Applications/VLC.app/Contents/MacOS/VLC "+str(vid_to_play))
    rate=0
    while True:
        try:
            rate=int(input("please enter a rating between 1 and 5    "))
            if rate>0 and rate<6:
                break
            else:
                print("please enter value between 1 and 5")
        except:
            print("please enter a valid integer")
    ratings[5].append(rate)
	
    #V7
    print("Playing Advertisement using Recommendation V7\n")
    vid_to_play=rec_v7.recommend(df_list_v7)
    os.system("/Applications/VLC.app/Contents/MacOS/VLC "+str(vid_to_play))
    rate=0
    
    while True:
        try:
            rate=int(input("please enter a rating between 1 and 5    "))
            if rate>0 and rate<6:
                break
            else:
                print("please enter value between 1 and 5")
        except:
            print("please enter a valid integer")
    ratings[6].append(rate)

    ##repeat?
    repeat=input("would you like to rate me again? y/n   ")
    x=1
    while x:
        if repeat!="y" and repeat!="n":
            print("please enter y or n")
            repeat=input("would you like to try me again? y/n   ")
        elif repeat=="y" or repeat=="n":
            x=0

#ratings info
maxi=0
mod=0

for rates in ratings:
    if maxi<mean(rates):
        maxi=mean(rates)
        mod=ratings.index(rates)
        
maxi_model=mod+1
print("The engine with the highest rating is version   " +str(maxi_model)+" with an average rating of "+str(maxi) )

store="y"
name="Anonymous"
print("Would you like us to store your statistics for our testing purposes")
store=input("Please enter y/n    ")
if store=="y":
    name=input("Enter your name    ")
    
with open("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ratings_/"+name+".txt","w") as f:
	s=1
	for rate in ratings:
		
		nw=" ".join(str(rate))
		f.write("V"+str(s)+" = "+nw+"\n")
		s+=1
	f.write("BEST = "+str(maxi_model))
	f.close()
