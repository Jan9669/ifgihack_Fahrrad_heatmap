#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[3]:


places_codes = [100034978, 100031300, 100034980, 100034982, 100053305, 100035541, 100031297, 100034983, 100034981]

places_names = ["100034978 - Gartenstraße",
               "101034978 - Gartenstraße einwärts",
               "102034978 - Gartenstraße auswärts", 
               "100031300 - Hafenstraße",
               "101031300 - Channel 1 IN", 
               "102031300 - Channel 2 OUT",
              "100034980 - Hammer Straße",
               "101034980 - Hammer Straße stadteinwärts",
               "102034980 - Hammer Straße stadtauswärts",
               "100034982 - Hüfferstraße",
               "101034982 - Hüfferstraße stadteinwärts",
               "102034982 - Hüfferstraße stadtauswärts",
               "100053305 - Kanalpromenade",
               "101053305 - Kanalpromenade Fahrräder Richtung Osttor",
               "102053305 - Kanalpromenade Fahrräder Richtung Zentrum",
               "103053305 - Kanalpromenade Fahrräder Richtung Osttor",
               "104053305 - Kanalpromenade Fahrräder Richtung Zentrum",
               "100035541 - Neutor",
               "101035541 - Neutor stadteinwärts",
               '102035541 - Neutor stadtauswärts',
               "100031297 - Promenade",
               "101031297 - Promenade Radfahrer FR Mauritztor",
               "102031297 - Promenade Radfahrer FR Salzstraße",
               "103031297 - Promenade Radfahrer FR Mauritztor",
               "104031297 - Promenade Radfahrer FR Salzstraße",
               "105031297 - Promenade Radfahrer FR Mauritztor",
               "106031297 - Promenade Radfahrer FR Salzstraße",
               "100034983 - Warendorfer Straße",
               "101034983 - Warendorfer Straße stadteinwärts",
               "102034983 - Warendorfer Straße stadtauswärts",
               "100034981 - Weseler Straße",
               "101034981 - Weseler Straße stadteinwärts",
               "102034981 - Weseler Straße stadtauswärts"]


# In[4]:


new_words = [item.strip().split() for item in places_names]
new_words

#create list with the same names that appear in the dataframe columns
places_names2 = []
for i in range(len(new_words)):
    if len(new_words[i]) == 7:
        word = new_words[i][0]+" "+"("+new_words[i][2]+" "+new_words[i][3]+" "+new_words[i][4]+new_words[i][5]+" "+new_words[i][6]+")"
        places_names2.append(word)
    elif len(new_words[i]) == 6:
        word = new_words[i][0]+" "+"("+new_words[i][2]+" "+new_words[i][3]+" "+new_words[i][4]+" "+new_words[i][5]+")"
        places_names2.append(word)
    elif len(new_words[i]) == 5:
        word = new_words[i][0]+" "+"("+new_words[i][2]+" "+new_words[i][3]+" "+new_words[i][4]+")"
        places_names2.append(word)
    elif len(new_words[i]) == 4:
        word = new_words[i][0]+" "+"("+new_words[i][2]+" "+new_words[i][3]+")"
        places_names2.append(word)
    elif len(new_words[i]) == 3:
        word = new_words[i][0]+" "+"("+new_words[i][2]+")"
        places_names2.append(word)


# In[49]:


def create_csv(code, date):
    #input 
    #name -> place name
    #date -> "mm-yyyy"
    
    #define patter of region
    code = str(code)
    str_match = [s for s in places_names2 if code[-5:] in s]
    
    
    #Reading dataframe (promenade)
    df = pd.read_csv(f"https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/{str(code)}/{str(date)}.csv")

    #remove status columns
    df = df[df.columns.drop(list(df.filter(regex='status')))]

    try:
        if len(str_match[-1].split()) == 5:
            #sum specific directions
            df[f"sum_{str_match[1]}"] = df[str_match[1]]+df[str_match[3]]+df[str_match[5]]
            df[f"sum_{str_match[2]}"] = df[str_match[2]]+df[str_match[4]]+df[str_match[6]]
        elif len(str_match[-1].split()) == 4:
            df[f"sum_{str_match[1]}"] = df[str_match[1]]
            df[f"sum_{str_match[2]}"] = df[str_match[2]]
        elif len(str_match[-1].split()) == 3:
            df[f"sum_{str_match[1]}"] = df[str_match[1]]
            df[f"sum_{str_match[2]}"] = df[str_match[2]]
    except:
        df[f"sum_{str_match[1]}"] = df[str_match[1]]+df[str_match[3]]
        df[f"sum_{str_match[2]}"] = df[str_match[2]]+df[str_match[4]]


    #sum every hour 
    #total
    df[f"sum_{str_match[0]}"] = df[str_match[0]].rolling(window=4).sum()

    #sum specific directions 
    df[f"sum_{str_match[1]}"] = df[f"sum_{str_match[1]}"].rolling(window=4).sum()
    df[f"sum_{str_match[2]}"] = df[f"sum_{str_match[2]}"].rolling(window=4).sum()


    #leave only the sum columns in the dataframe
    df.rename(columns={"Datetime":"sum_Datetime"}, inplace=True)
    df = df.loc[:,df.columns.str.startswith('sum')]

    #keep only 00:45 sum results
    df = df[df['sum_Datetime'].str.contains(':45')]
    

    #create f string name place and date 
    df.to_csv(rf"D:\Users\Igor_Quaresma_D\Documents\Visual Code\Hackifgi\Hack\results\cleaned_datasets\{code}\{code}-{date}.csv")


# In[20]:


dates = ["2019-01",
"2019-02",
"2019-03",
"2019-04",
"2019-05",
"2019-06",
"2019-07",
"2019-08",
"2019-09",
"2019-10",
"2019-11",
"2019-12",
"2020-01",
"2020-02",
"2020-03",
"2020-04",
"2020-05",
"2020-06",
"2020-07",
"2020-08",
"2020-09",
"2020-10",
"2020-11",
"2020-12",
"2021-01",
"2021-02",
"2021-03",
"2021-04",
"2021-05",
"2021-06",
"2021-07",
"2021-08",
"2021-09",
"2021-10",
"2021-11",
"2021-12",
"2022-01",
"2022-02",
"2022-03",
"2022-04",
"2022-05",
"2022-06",
"2022-07",
"2022-08",
"2022-09",
"2022-10",
"2022-11",
"2022-12",
"2023-01",
"2023-02",
"2023-03"]


# In[53]:


for i in dates:
    create_csv(100031300, i)


# In[ ]:




