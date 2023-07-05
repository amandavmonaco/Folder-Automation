import numpy as np
import pandas as pd
import os
import shutil
from ListOfInvestors import *

# path = '/Users/amandamonaco/Documents/Folder-Automation'

# print("Before moving file: ")
# print(os.listdir(path))



def InvestorData() :
    try: 
        excelFile = pd.read_excel("InvestorPropertisPyFile.xlsx")
        # print(excelFile)
    except FileNotFoundError:
        print('Financial distribution file not found')

    investorKeyDictionary = {}

    for column in excelFile:
        column_values = excelFile[column].tolist()
        filtered_values = [value for value in column_values if not pd.isnull(value)]
        investorKeyDictionary[column] = filtered_values

    #Checking that the dictionary is correct
    for keys, values in investorKeyDictionary.items():
        print(keys, ": ", values)
    
    propertyKeyDictionary = {}

    # for key,values in investorKeyDictionary.items():
    #     for i in range(0, len(values)-1):
    #         newKey = list(investorKeyDictionary.keys()[i])
    #         print(newKey)
    #         propertyKeyDictionary[investorKeyDictionary[property]] = [key]

    print("\nPROPERTY KEY DICTIONARY:\n")
    for keys, values in propertyKeyDictionary.items():
        print(keys, ": ", values) 

    for i in range(0, len(InvestorNames)-1):   
        print(InvestorNames[i])


    for i in range(0, len(InvestorNames)-1):
       investorName = InvestorNames[i]
       allKeys = list(investorKeyDictionary.keys())
       print("ALL KEYS:\n")
       print(allKeys)
       for j in range(0, len(allKeys)-1):
            print (allKeys[j])
            listOfOneInvestorsProperties = investorKeyDictionary[allKeys[j]]
            print(listOfOneInvestorsProperties)
            # for k in range(0, len())
            #     propertyKeyDictionary[]


    investorList = []
    root_directory = 'Investor Financial Data'
    for investor in investorKeyDictionary.keys():
        for properties in investorKeyDictionary[investor]:
            dir_name = str(root_directory) + '/' + str(investor) + '/' + str(properties)
            try:
                os.makedirs(dir_name)
                print('Directory ' + dir_name + ' created')
            except FileExistsError:
                print('Directory ' + dir_name + ' already exists') 
   
    
       
    # word_to_find = "InvestorData"
    # InvestorNamesRow = excelFile.contains(word_to_find, na=False)
    # print(InvestorNamesRow)


InvestorData()

# Determine which properties are current
# Create a folder for each of these properties
# Create a folder for each investors within a root folder called Investor Financial Reports
# Create a dictionary with properties as the key and list of investors as the value
# Populate all of the properties folders with the relevant files from the folder



