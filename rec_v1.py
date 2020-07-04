#V1
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os
from glob import glob

def recommend(input_data):
    ranks={"genre":[],"vid":[],"rate":[]}
    for inpu in input_data:
        ds=pd.DataFrame(columns=["id","description"])
        input_split=inpu.split("/")
        test_path="/Volumes/SkAnDH_Xb/final_year_pj/R2_/test_data/test_vids_all_data/"+input_split[0]+"/"
        ad_path="/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_all_data/"+input_split[0]+"/"
        test=test_path+str(input_split[1].replace(".avi",".txt"))
        ads=[y for x in os.walk(ad_path) for y in glob(os.path.join(x[0], '*_v1.txt'))]
        #remove this for v2-v7
        dat=""
        try:
            with open(test,"r") as f:
                dat=f.readlines()
                f.close()
        except:
            test=test_path+str(input_split[1].replace("_v1.txt","_desc.txt"))
            with open(test,"r") as f:
                dat=f.readlines()
                f.close()
        data=[]
        for i in dat:
            data.append(i.split(" "))
        data=[j.replace("\n","") for i in data for j in i]
        test_data=list(filter(None,data))
        test_data=list(set(test_data))
        test_data=" ".join(test_data)
        ad_data=""
        s=0
        for a in ads:
            with open(a,"r") as f:
                ad_data=f.readlines()
                ad_data=list(set(ad_data))
                ad_data=" ".join(ad_data)
                ad_data=ad_data.replace("\n","")
            id_=a.replace(ad_path,"")
            id_=id_.replace("_v1.txt","")
            
            col1=s
            col2=id_+" - "+ad_data
            ds.loc[s,"id"]=s
            ds.loc[s,"description"]=col2
            s+=1
        col2=id_+" - "+test_data
        ds.loc[s,"id"]=s
        ds.loc[s,"description"]=col2
        score_=0
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(ds['description'])

        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        results = {}

        for idx, row in ds.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
            similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

            results[row['id']] = similar_items[1:]
        re_top=[]
        def item(id):
            re_top.append(ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0])
            return ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]

        # Just reads the results out of the dictionary.
        def recommend(item_id, num):
            #print("Recommending " + str(num) + " ads similar to " + item(item_id) + "...")
            item(item_id)
            #print("-------")
            recs = results[item_id][:num]
            ranks["rate"].append(results[item_id][:num][0][0])
            #for rec in recs:
                #print("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")

        recommend(item_id=s, num=5)
        ranks["genre"].append(input_split[0])
        ranks["vid"].append(re_top[0])
    max_=ranks["rate"].index(max(ranks["rate"]))
    gen=ranks["genre"][max_]
    numb=ranks["vid"][max_]
    video_path="/Volumes/SkAnDH_Xb/final_year_pj/R2_/ads/r2_avi/"+gen+"/"+numb+".avi"
    return video_path
