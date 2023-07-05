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
        excelFile = pd.read_excel("InvestorPropertiesPyFile.xlsx")
    except FileNotFoundError:
        print('Financial distribution file not found')

    investorKeyDictionary = {}

    for column in excelFile:
        column_values = excelFile[column].tolist()
        filtered_values = [value for value in column_values if not pd.isnull(value)]
        investorKeyDictionary[column] = filtered_values

    properties = set()
    root_directory = 'Investor Financial Data'
    for investor in investorKeyDictionary.keys():
        for property in investorKeyDictionary[investor]:
            properties.add(property)
            dir_name = str(root_directory) + '/' + str(investor) + '/' + str(property)
            try:
                os.makedirs(dir_name)
                print('Directory ' + dir_name + ' created')
            except FileExistsError:
                print('Directory ' + dir_name + ' already exists') 
    
    # for i in properties:
    #     print(i)
    sourcePath = '/Users/amandamonaco/Documents/Folder Automation/12Month'
    
    
    for fileName in os.scandir(sourcePath):
        if fileName.is_file():
            print(fileName)
            f = str(fileName)
            endingIndex = f.find('12')
            # singleQuote = f.find('\'')
            # doubleQuote = f.find('\"')
            startingIndex = 11 
      
            print(startingIndex, " " ,endingIndex)
            print(f[startingIndex:endingIndex])
            for p in properties: 
                if str(p) == fileName:
                    print('P: ' + p)
                
    

    
    # print(os.listdir(sourcePath))


InvestorData()

# Determine which properties are current
# Create a folder for each of these properties
# Create a folder for each investors within a root folder called Investor Financial Reports
# Create a dictionary with properties as the key and list of investors as the value
# Populate all of the properties folders with the relevant files from the folder



