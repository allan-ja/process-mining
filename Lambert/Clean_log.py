# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:08:34 2016

@author: geoaj
"""

import pandas as pd


def extractDrawingNumber(description):
    wordList = description.split()
    filteredList = list()
    for word in wordList:
        if (containsNumber(word) >= 4):           
           filteredList.append(word)
   
    return " ".join(filteredList)
    
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def containsNumber(word):
    i = 0
    for letter in word:
        if isNumber(letter):
            i = i+1
    return i
        
df = pd.read_excel("./Raffa log.xlsx")

df2 = df[df['Unit Price'] == 0]

df3 = df2.drop(df.columns[[0,1,6,7,11,12,13,14]], axis=1)

df3['Description'] = df['Description'].apply(extractDrawingNumber)
df3.rename(columns={'Description' : 'Drawing'}, inplace = True)

poVSdrawing = df3.groupby('P/O No.').Drawing.nunique()
drawingVSpo = df

nDesc = pd.value_counts(df3.Drawing.values)

df5 = pd.crosstab(df3['P/O No.'], df3.Drawing)

count = df3.groupby('P/O No.').count()
