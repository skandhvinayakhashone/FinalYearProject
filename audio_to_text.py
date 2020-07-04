import speech_recognition as sr
import ffmpy
import os
from glob import glob

#Audio to text of test data

try:
	inp=sys.argv[1]
    try:
        op=inp.replace(".avi",".wav")
        os.system("ffmpeg -i "+inp+" -f wav -vn "+"./"+i+".wav")
    except:
        print(op)

	os.system("ffmpeg -i "+inp+" -f wav -vn " +inp+".wav")


	##ads conversion
	 
	def convert(file_):
	    t=""
	    sound = file_
	    r = sr.Recognizer()
	    with sr.AudioFile(sound) as source:
	        r.adjust_for_ambient_noise(source)
	        audio = r.listen(source)
	    try:
	        t=r.recognize_google(audio)
	    except Exception as e:
	        pass
	    return t


	txt=convert(inp+".wav")
	pat="."
	pat=pat.replace(".wav","_audio_to_txt.txt")
	with open(pat,"w+") as f:
	    try:
	        zen=txt.split(" ")
	        for z in zen:
	            f.write(str(z)+"\n")
	    except:
	        print(fil)
	    f.close()

except:
# Video to audio of all datasets

dir_list=os.listdir("/Volumes/SkAnDH_Xb/final_year_pj/R2_/r2_wav/")
for i in dir_list:
    files=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/r2_avi/"+i+"_avi") for y in glob(os.path.join(x[0], '*.avi'))]
    for fil in files:
        try:
            op=fil.replace(".avi",".wav")
            op=op.replace("/Volumes/SkAnDH_Xb/final_year_pj/R2_/r2_avi/"+i+"_avi/","")
            os.system("ffmpeg -i "+fil+" -f wav -vn "+"/Volumes/SkAnDH_Xb/final_year_pj/R2_/r2_wav/"+i+"/"+op)
        except:
            print(op)


files=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_vids_avi/") for y in glob(os.path.join(x[0], '*.avi'))]

s=0
for fil in files:
    os.rename(fil,"/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_vids_avi/"+str(s)+".avi")
    s+=1

for fil in files:
    try:
        op=fil.replace(".avi",".wav")
        op=op.replace("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_vids_avi/","")
        os.system("ffmpeg -i "+fil+" -f wav -vn "+"/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_vids_wav/"+op)
    except:
        print(op)


##ads conversion
 
def convert(file_):
    t=""
    sound = file_
    r = sr.Recognizer()
    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        t=r.recognize_google(audio)
    except Exception as e:
        pass
    return t


dir_list=os.listdir("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_wav/")
for i in dir_list:
    os.makedirs("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_all_data/"+i)
    files=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_wav/"+i) for y in glob(os.path.join(x[0], '*.wav'))]
    for fil in files:
        txt=convert(fil)
        pat=fil.replace("/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_wav/","/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_all_data/")
        pat=pat.replace(".wav","_audio_to_txt.txt")
        with open(pat,"w+") as f:
            try:
                zen=txt.split(" ")
                for z in zen:
                    f.write(str(z)+"\n")
            except:
                print(fil)
            f.close()


dir_list=os.listdir("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_wav/")
for i in dir_list:
    files=[y for x in os.walk("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_wav/"+i) for y in glob(os.path.join(x[0], '*.wav'))]
    for fil in files:
        txt=convert(fil)
        pat=fil.replace("/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_wav/","/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_all_data/")
        pat=pat.replace(".wav","_audio_to_txt.txt")
        with open(pat,"w+") as f:
            try:
                zen=txt.split(" ")
                for z in zen:
                    f.write(str(z)+"\n")
            except:
                print(fil)
            f.close()


