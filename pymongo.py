#!/usr/bin/env python
# coding: utf-8

# # Loading the Data

# In[1]:


# importing libraries
import pymongo
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


# In[2]:


# parsing
tree=ET.parse('dblp.XML') ### XML File
root=tree.getroot()
print(root)


# In[2]:


# storing in mongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")   ### specify URI for mongoDB you want to connect to
db = client ["DB"]     #create DB
coll = db["DBLP_DATA"]   #create colection

for i in range( 0, len(list(root)) ):
    dic={}
    dic["Element-Type"]=root[i].tag
    for x in root[i]:
        try:
            dic[x.tag]= int(x.text)
        except:
            dic[x.tag]= x.text
    coll.insert_one(dic)