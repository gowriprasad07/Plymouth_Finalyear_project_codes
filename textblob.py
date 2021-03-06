# -*- coding: utf-8 -*-
"""TextBlob

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hC2dBp7T9701S7LzFjtNT1XtMoUBgIdz
"""

!pip install textblob

from textblob import TextBlob
from pickle import dump,load
import time

from google.colab import drive
drive.mount('/content/gdrive')

f=open("/content/gdrive/My Drive/Colab Notebooks/VADER_File.pickle","rb")

a=load(f)
print(a)

TextBlob(a["tweet_text"]).sentiment.polarity

def srt(pol):
    if pol>0:
        return "pos"
    elif pol<0:
        return "neg"
    else:
        return "neu"

def serl(lt):
    
    temp=''
    for i in lt:
        temp+=(i+" ")
    return temp[:-1]

count,over_ct=0,0
f=open("/content/gdrive/My Drive/Colab Notebooks/VADER_File.pickle","rb")

f_dict={}
full=[]

while 1:
    try:
        a=load(f)
        full.append(a)
    except EOFError:
        break

len(full)
print("DOne Loading")

start_time=time.time()

for a in full:
    try:
        #a=load(f)
        if a["tweet_id"] not in f_dict:
            """
            f_dict[a["tweet_id"]]={"tweet_text":srt(TextBlob(a["tweet_text"]).sentiment.polarity),
                                   "snowball":srt(TextBlob(serl(a["snowball"])).sentiment.polarity),
                                   "porter":srt(TextBlob(serl(a["porter"])).sentiment.polarity)}
            """
            f_dict[a["tweet_id"]]={"porter":srt(TextBlob(serl(a["porter"])).sentiment.polarity)}
            count+=1
        else:
            print(a["tweet_id"]," is copy")
    except EOFError:
        break
    """
    if count==100000:
        over_ct+=1
        print(over_ct)
        count=0
    """
end_time=time.time()
print(end_time-start_time)
print(len(f_dict))

c=0
for i in f_dict:
    print(i,f_dict[i])
    c+=1
    if c==5:
        break

a

len(f_dict)

nff=open("/content/gdrive/My Drive/Colab Notebooks/Post_textblob.pickle","wb")

dump(f_dict,nff)

nff.close()

