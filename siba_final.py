
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df1=pd.read_csv('symptoms.csv')
df2=pd.read_csv('sym_dia_final.csv')


# In[2]:


text=input("Enter the string")
#text
#tokens=[t for t in text.split()]
from nltk.tokenize import word_tokenize as wt
tokens=wt(text)


# In[3]:


#tokens
cleantokens=tokens[:]
from nltk.corpus import stopwords
sw=stopwords.words('english')
for tok in tokens:
    if tok in stopwords.words('english'):
        cleantokens.remove(tok)


# In[5]:


from nltk.stem import PorterStemmer,WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
stemmer=PorterStemmer()
finals=[]
for root in cleantokens:
    #finals.append(lemmatizer.lemmatize(root))
    finals.append(stemmer.stem(root))
finset=set()
#finals


# In[6]:


for index,rows in df1.iterrows():
    for far in finals:
        if far in rows['symptom']:
            finset.add(rows['sid'])
#finset


# In[7]:


anslist=[]
df3=pd.DataFrame(columns=[['sid','did', 'wei']])
#df3.head()


# In[8]:


for stat in finset:
    for i in range(len(df2.index)):
        if df2.loc[i, 'sid'] == stat:
            df3.loc[i, 'sid'] = df2.loc[i, 'sid']
            df3.loc[i, 'did'] = df2.loc[i, 'did']
            df3.loc[i, 'wei'] = df2.loc[i, 'wei']


# In[9]:


#df3.head(20)
#df3=df3.iloc[:,[0,1]]
#df3.dtypes


# In[10]:


df3.to_csv('sym_dia_res2.csv', index=False)
df4=pd.read_csv('sym_dia_res2.csv')
df4=df4.sort_values(by='wei',ascending=False)
print("HERE IS THE ELENGTH")
print(len(df4))


# In[11]:



df5=pd.read_csv('diagonistics.csv')
df6=pd.read_csv('med_final.csv')


# In[12]:


print("You may be affected with (with decreasing probability)")
for x in range(5):
    indic=df3.iloc[x,1]
    print ("Case ",end=' ')
    print(x+1,end=' - ')
    for i in range(len(df5.index)):
        if df5.loc[i,'did']==indic:
            print(df5.loc[i,'diagnosis'])
    
    for i in range(len(df6.index)):
        if df6.loc[i,'did']==indic:
            print("     Treatment is",end=' ')
            print(df6.loc[i,'medicine'])
    

