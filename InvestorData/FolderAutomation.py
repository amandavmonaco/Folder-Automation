import os 
import shutil
import pandas as pd

financialDocumentsPath = '/Users/amandamonaco/Documents/Folder Automation/12Month'
propertyKeyDictionary = {}

def CreateInvestorPropertyDictionary():
    try:
        excelFile = pd.read_excel('InvestorPropertiesPyFile.xlsx')
    except FileNotFoundError:
        print('Investor Properties File was not found')

    for column in excelFile:
        column_values = excelFile[column].tolist()
        filtered_values = [value for value in column_values if not pd.isnull(value)]
        propertyKeyDictionary[column] = filtered_values

def TestFunctionToPrintDictionary():
    for propertyKey in propertyKeyDictionary.keys():
        print('KEY: ' + propertyKey)
        for investors in propertyKeyDictionary[propertyKey]:
            print(' INVESTOR: ' + investors)


def CreatePropertyFoldersWithFinancialStatements():
    root_dir = 'Property Folders'
    for fileName in os.scandir(financialDocumentsPath):
        if fileName.is_file():
            f = str(fileName)
            endingIndex = f.find('12') - 1
            findDash = f.find('-')
            if(findDash != -1):
                endingIndex = findDash
            startingIndex = 11

            trimmedFileName = f[startingIndex:endingIndex]
            trimmedFileName[:-1]
            
            propFolderName = str(root_dir) + '/' + str(trimmedFileName)
            try:
                os.makedirs(propFolderName)
                print(propFolderName+ ' made')
            except FileExistsError:
                print('Folder', trimmedFileName, 'already exists')
                
            shutil.copy(fileName, propFolderName)


def CreateInvestorFoldersWithPropertyStatements():
    root_dir = 'Investor Folders'

    for folder in os.scandir('Property Folders'):
        investorNames = propertyKeyDictionary.get(folder.name)
        if investorNames != None:  
            for i in investorNames:
                try: 
                    path = os.makedirs(str(root_dir) + '/' + i)
                except FileExistsError:
                    print(i + ' folder already created')
                shutil.copytree('Property Folders/' + folder.name, 'Investor Folders/' + i + '/' + folder.name)
                
                


CreateInvestorPropertyDictionary()
CreatePropertyFoldersWithFinancialStatements()
CreateInvestorFoldersWithPropertyStatements()