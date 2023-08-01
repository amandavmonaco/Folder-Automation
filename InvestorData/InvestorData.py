import numpy as np
import pandas as pd
import os
import shutil
from ListOfInvestors import *


sourcePath = '/Users/amandamonaco/Documents/Folder Automation/12Month'
investorKeyDictionary = {}

def InvestorData() :
    root_dir = 'Property Financial Statements'

    try: 
        excelFile = pd.read_excel("InvestorPropertiesPyFile.xlsx")
    except FileNotFoundError:
        print('Financial distribution file not found')

    

    for column in excelFile:
        column_values = excelFile[column].tolist()
        filtered_values = [value for value in column_values if not pd.isnull(value)]
        investorKeyDictionary[column] = filtered_values
       

    root_directory = 'Investor Financial Data'
    for investor in investorKeyDictionary.keys():
        print(investor)
        for property in investorKeyDictionary[investor]:
            dir_name = str(root_directory) + '/' + str(investor) + '/' + str(property)
            src_name = str(root_dir) + '/' + str(property)
            try:
                os.makedirs(dir_name)
                print('Directory ' + dir_name + ' created')
            except FileExistsError:
                # print('Directory ' + dir_name + ' already exists')     
                val=1
    
    root_dir = 'Property Financial Statements'
    for fileName in os.scandir(sourcePath):
        if fileName.is_file():
            f = str(fileName)
            endingIndex = f.find('12') - 1
            findDash = f.find('-')
            if(findDash != -1):
                endingIndex = findDash
            startingIndex = 11

            trimmedFileName = f[startingIndex:endingIndex]
            
            propFolderName = str(root_dir) + '/' + str(trimmedFileName)
            try:
                os.makedirs(propFolderName)
                print(propFolderName+ ' made')
            except FileExistsError:
                # print('Folder', trimmedFileName, 'already exists')
                val=1

            shutil.copy(fileName, propFolderName)
    


fileDictionary = {}

# def PopulatePropertyFolders():
    # for investor in investorKeyDictionary.keys():
    #     print('1: ' + investor)
    #     for property in investorKeyDictionary[investor]:
    #         print('2: ' +property)
    #         for entry in os.scandir('Investor Financial Data'):
    #             print('3: ' + entry.name)
    #             for entry2 in os.scandir('Investor Financial Data/' + entry.name):
    #                 print('4: ' + entry2.name)
    #                 if entry2.name == property:
    #                     shutil.move('Property Financial Statements/'+str(property), 'Investor Financial Data/' + entry.name)
                        

def PopulatePropertyFolders():
    for entry in os.scandir('Property Financial Statements'):
        print('1: ' + entry.name)
        for investor in investorKeyDictionary.keys():
            for property in investorKeyDictionary[investor]:
                print(property)
                if property==entry.name:
                    print(property + ' MATCHED ' +  entry.name)
                    shutil.copytree('Property Financial Statements/'+entry.name+' 12 Month Statement 05.30.2023.xlsx', 'Investor Financial Data/'+investor+'/'+entry.name, dirs_exist_ok=True)
                    
                       
                            

                   


# InvestorData()
PopulatePropertyFolders()


# Determine which properties are current
# Create a folder for each of these properties
# Create a folder for each investors within a root folder called Investor Financial Reports
# Create a dictionary with properties as the key and list of investors as the value
# Populate all of the properties folders with the relevant files from the folder



