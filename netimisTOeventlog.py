# -*- coding: utf-8 -*-

import pandas as pd
# FUNCTION DEFINITIONS
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


# CONSTANT VARIABLES    
COLUMNS_TO_EXCLUDE = ['Patient','All Paths','Outcome','Time (hr)', 'Cost (GBP)']

# Clear global variable
if 'eventList' in globals(): del eventList

# Import CSV file as pandas.DataFrame
df = pd.read_csv('./report_systemflow.csv')

columns = ["Patient", "Activity"]

df.apply(splitPath, axis=1)
eventdf = pd.DataFrame(eventList, columns = columns)




nam = df.columns.values
attributeList = nam.tolist()

for columns in COLUMNS_TO_EXCLUDE:
    attributeList.remove(columns)
    

patientList = df.Patient.values
for patient in patientList:
    for attribute in attributeList:    
        value = df[df.Patient == patient].iloc[0][attribute]
        eventdf.loc[eventdf.Patient == patient, attribute] = value
   