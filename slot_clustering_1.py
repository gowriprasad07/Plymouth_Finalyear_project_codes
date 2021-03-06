# -*- coding: utf-8 -*-
"""Slot_Clustering_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NSh82d8_18pfj5_2WraxWnxOseMFW71V
"""

#Combined Code to both to segregate the tweets into 6min slots each and also to store the final clusters
#Need to run it on both Snowball and Porter versions of the text.

from google.colab import drive
drive.mount('/content/gdrive')

from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import load,dump

f=open("/content/gdrive/My Drive/Colab Notebooks/Hourly_Slots.pickle","rb")
d_h=load(f)
f.close()

d_h[20][0]

#Each list entry : tweet_id,user_id,tweet_text,tweet_created_at,snowball,porter

#Minute slot Dict.

mod={}

for i in d_h:

    temp={}
    for j in d_h[i]:
        if j[3].minute//6 not in temp:
            temp[j[3].minute//6]=[j]
        else:
            temp[j[3].minute//6].append(j)
    mod[i]=temp

####################################################
#Porter Section   ##Using minute slots
#Cosine similarity can be caluclated later.
###################################################

d_h=0
atot=[]

from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import dump,load
#ff=open("/content/gdrive/My Drive/Colab Notebooks/Post_TFIDF.pickle","wb")


#Mention Hour slot here. iterate through the list in chronology one by one.
for hour in [3]:

  #ff=open("/content/gdrive/My Drive/Colab Notebooks/TF_IDF/Res_"+str(hour)+".pickle","wb")
  for mint in mod[hour]:
    vec=TfidfVectorizer(ngram_range=(2,3),min_df=7)
    vec_f=vec.fit_transform([j[-1] for j in mod[hour][mint]]).toarray()
    #tempd={}
    #tempd[mint]=[vec_f,vec.get_feature_names()]
    #dump([mint,[vec_f],[vec.get_feature_names()],[j[0] for j in mod[hour][mint]]],ff)
    atot.append([mint,[vec_f],[vec.get_feature_names()],[j[0] for j in mod[hour][mint]]])
    #tempd={}
    print(hour," ",mint," ",len(mod[hour][mint]),len(vec.get_feature_names()))

import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

nf=open("/content/gdrive/My Drive/Colab Notebooks/Porter/"+str(hour)+".pickle","wb")


for a in atot:
  print("\n\n")
  sm=cosine_similarity(a[1][0])
  pd.set_option('display.max_rows', 10)
  v=pd.DataFrame(sm,columns=a[-1], index=a[-1])

  print("Cosine Similarity done for ",hour," ",a[0])
  print(len(a[-1]))


  from scipy.cluster.hierarchy import dendrogram, linkage

  lk=linkage(sm,"ward")
  #pd.DataFrame(lk,columns=['Document\Cluster 1', 'Document\Cluster 2','Distance', 'Cluster Size'],dtype='object')
  #lk

  b=list(lk)

  dist,mn,mx=0,0,0

  for i in range(len(b[:-1])):
    
    if b[i+1][-2]-b[i][-2]>dist:
      dist=b[i+1][-2]-b[i][-2]
      mn=b[i][-2]
      mx=b[i+1]
      mn=b[i]


  from scipy.cluster.hierarchy import fcluster
  
  cluster_labels = fcluster(lk, int(mn[-2]+1), criterion='distance')

  cluster_labels1 = pd.DataFrame(cluster_labels, columns=['ClusterLabel'],index=a[-1])
  pd.set_option('display.max_rows',200 )

  print(set(cluster_labels))

  dump([a[0],cluster_labels,a[-1]],nf)

  print("\nClustering Done!")

nf.close()
print("Completed")

len(cluster_labels)

hello

test

for i in mn:
  print(i)