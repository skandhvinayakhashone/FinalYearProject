from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
import os
from glob import glob
import cv2
import enchant
import sys

#convert video frames to text

try:
    inp=sys.argv[1]

    def vid_to_text(vid):
        if not os.path.exists('image_frames'):
            os.makedirs('image_frames')
        test_vid = cv2.VideoCapture(vid)
        index = 0
        while test_vid.isOpened():
            ret,frame = test_vid.read()
            if not ret:
                break
            name = './image_frames/frame' + str(index) + '.png'
            cv2.imwrite(name, frame)
            index = index + 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break    
        test_vid.release()
        cv2.destroyAllWindows()
        vid_images=[y for x in os.walk("./image_frames/") for y in glob(os.path.join(x[0], '*.png'))]
        fi_li=[]
        for v in range(0,len(vid_images),20):
            demo = Image.open(vid_images[v])
            text = pytesseract.image_to_string(demo, lang = 'eng')
            l1=list(filter(None,text.split("\n")))
            l2=[x for x in l1 if x!=" "]
            fi_li.append(l2)
        os.system("rm -r image_frames")
        final_list=[j for i in fi_li for j in i]
        return final_list

        d = enchant.Dict("en_US")


    spec_car="!@#$%^&*(){}:,>.<|\\+=_-~`\"\';?/[]"
    dir_list=['fashion',
     'sports',
     'gaming',
     'food',
     'tech',
     'movies',]
    txt_list=vid_to_text(inp)
    txt=" ".join(txt_list)
    pat="."
    with open(pat,"w+") as f:
        zen=txt.split(" ")
        for z in zen:
            if z!="" and z!=" ":
                if d.check(z) and z not in spec_car and len(z)>2 :
                    f.write(str(z)+"\n")
        f.close()
    print(fil)

    
except:
    def vid_to_text(vid):
        if not os.path.exists('image_frames'):
            os.makedirs('image_frames')
        test_vid = cv2.VideoCapture(vid)
        index = 0
        while test_vid.isOpened():
            ret,frame = test_vid.read()
            if not ret:
                break
            name = './image_frames/frame' + str(index) + '.png'
            cv2.imwrite(name, frame)
            index = index + 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break    
        test_vid.release()
        cv2.destroyAllWindows()
        vid_images=[y for x in os.walk("./image_frames/") for y in glob(os.path.join(x[0], '*.png'))]
        fi_li=[]
        for v in range(0,len(vid_images),20):
            demo = Image.open(vid_images[v])
            text = pytesseract.image_to_string(demo, lang = 'eng')
            l1=list(filter(None,text.split("\n")))
            l2=[x for x in l1 if x!=" "]
            fi_li.append(l2)
        os.system("rm -r image_frames")
        final_list=[j for i in fi_li for j in i]
        return final_list


    d = enchant.Dict("en_US")

    #store all dataset in text files

    spec_car="!@#$%^&*(){}:,>.<|\\+=_-~`\"\';?/[]"
    dir_list=['fashion',
     'sports',
     'gaming',
     'food',
     'tech',
     'movies',]
    for i in dir_list:
        print(i)
        files=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_mp4/"+i) for y in glob(os.path.join(x[0], '*.mp4'))]
        for fil in range(14,len(files)):
            txt_list=vid_to_text(files[fil])
            txt=" ".join(txt_list)
            pat="/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_all_data/"+i+"/"+str(fil)+"_text.txt"
            with open(pat,"w+") as f:
                zen=txt.split(" ")
                for z in zen:
                    if z!="" and z!=" ":
                        if d.check(z) and z not in spec_car and len(z)>2 :
                            f.write(str(z)+"\n")
                f.close()
            print(fil)

    spec_car="!@#$%^&*(){}:,>.<|\\+=_-~`\"\';?/[]"
    dir_list=['fashion',
     'sports',
     'gaming',
     'food',
     'tech',
     'movies',]
    for i in dir_list:
        print(i)
        files=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_mp4/"+i) for y in glob(os.path.join(x[0], '*.mp4'))]
        for fil in range(len(files)):
            txt_list=vid_to_text(files[fil])
            txt=" ".join(txt_list)
            pat="/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_all_data/"+i+"/"+str(fil)+"_text.txt"
            with open(pat,"w+") as f:
                zen=txt.split(" ")
                for z in zen:
                    if z!="" and z!=" ":
                        if d.check(z) and z not in spec_car and len(z)>2 :
                            f.write(str(z)+"\n")
                f.close()
            print(fil)

