import numpy as np
import pandas as pd
import os
import shutil
from ListOfInvestors import *


sourcePath = '/Users/amandamonaco/Documents/Folder Automation/12Month'

def InvestorData() :
    root_dir = 'Property Financial Statements'

    for fileName in os.scandir(sourcePath):
        if fileName.is_file():
            f = str(fileName)
            endingIndex = f.find('12')
            findDash = f.find('-')
            if(findDash != -1):
                endingIndex = findDash
            startingIndex = 11

            trimmedFileName = f[startingIndex:endingIndex]
            propFolderName = str(root_dir) + '/' + str(trimmedFileName)
            try:
                os.makedirs(propFolderName)
            except FileExistsError:
                print('Folder ', trimmedFileName, ' already exists')

            shutil.copy(fileName, propFolderName)


    try: 
        excelFile = pd.read_excel("InvestorPropertiesPyFile.xlsx")
    except FileNotFoundError:
        print('Financial distribution file not found')

    investorKeyDictionary = {}

    for column in excelFile:
        column_values = excelFile[column].tolist()
        filtered_values = [value for value in column_values if not pd.isnull(value)]
        investorKeyDictionary[column] = filtered_values

    root_directory = 'Investor Financial Data'
    for investor in investorKeyDictionary.keys():
        for property in investorKeyDictionary[investor]:
            dir_name = str(root_directory) + '/' + str(investor) + '/' + str(property)
            src_name = str(root_dir) + '/' + str(property)
            try:
                os.makedirs(dir_name)
                print('Directory ' + dir_name + ' created')
            except FileExistsError:
                print('Directory ' + dir_name + ' already exists')     
    

def PopulatePropertyFolders():
    print(os.listdir(sourcePath))
    for fileName in os.scandir(sourcePath):
        print(fileName)
        




# InvestorData()
PopulatePropertyFolders()


# Determine which properties are current
# Create a folder for each of these properties
# Create a folder for each investors within a root folder called Investor Financial Reports
# Create a dictionary with properties as the key and list of investors as the value
# Populate all of the properties folders with the relevant files from the folder



