# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
import csv
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
class text_analyzer(object):
    def __init__(self, text) :
        self.text = text
        #formatted text to replace such punctuation then convert the whole data into lower case 
        #for better understanding the client
        formatted_text = text.replace(".","").replace("!","").replace("?","").replace(",","")
        formatted_text = formatted_text.lower()
        self.fmtText = formatted_text
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word) #count method for counting the occurence
        return freqMap  # returning frequency dict
        
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

file_path = '/kaggle/input/customer-feedback-dataset/sentiment-analysis.csv'
df = pd.read_csv(file_path, header = None) 
# Combine all rows into a single text string
text_data = ' '.join(df.iloc[:, 0].astype(str))

analyzed = text_analyzer(text_data)
print("Formatted Text:\n", analyzed.fmtText)

freqMap = analyzed.freqAll()
print(freqMap)
word = "negative"
frequency = analyzed.freqOf(word)
print("\nThe word",word,"appears",frequency,"times.")