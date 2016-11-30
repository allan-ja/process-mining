# -*- coding: utf-8 -*-

import pandas as pd

def declareEventList():
    global eventList
    eventList = []
    return

def splitPath (record):
    # Declare eventList of does not exist
    if 'eventList' not in globals(): declareEventList()
    
    pathsList = record['All Paths'].split(', ')
    for path in pathsList:
        eventList.append( (record.Patient, path))
        
    eventList.append( (record.Patient, record.Outcome))
    return


    
COLUMNS_TO_EXCLUDE = ['Patient','All Paths','Outcome','Time (hr)', 'Cost (GBP)']
if 'eventList' in globals(): del eventList

df = pd.read_csv('./report4.csv')#, index = 'Patient')

columns = ["Patient", "Activity"]

df.apply(splitPath, axis=1)
eventdf = pd.DataFrame(eventList, columns = columns)

nam = df.columns.values
attributeList = nam.tolist()
#
#for columns in COLUMNS_TO_EXCLUDE:
#    attributeList.remove(columns)
#    
#
#patientList = df.Patient.values
#eventdf['Sex'] = 
#   