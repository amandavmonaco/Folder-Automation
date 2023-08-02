import os 
import shutil
import pandas as pd
from MonthAndYearFormat import *

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


def CreatePropertyFolders():
    root_dir = MonthYearFormat() + '/Property Folders'

    for property in propertyKeyDictionary.keys():
        folderName = str(root_dir) + '/' + str(property)
        try: 
            os.makedirs(folderName)
        except:
            print(property + ' Directory Exists')

balanceSheetsPath = 'Bal Sheet'
rentRollPath = 'Rent Roll'
ytdPath = 'YTD'

def BalanceSheet():
   dest_dir = MonthYearFormat() + '/Property Folders'

   for file in os.scandir(balanceSheetsPath):
       if file.is_file():
           temp = str(file)
           endingIndex = temp.find('Balance Sheet') - 1
           trimmedName = temp[11:endingIndex]
           destination = dest_dir + '/' + trimmedName
           if os.path.exists(destination):
                shutil.copy(file, destination)
           else:
                os.makedirs(dest_dir + '/' + trimmedName)
                shutil.copy(file, dest_dir + '/' + trimmedName)

def IncomeStatement():
   dest_dir = MonthYearFormat() + '/Property Folders'

   for file in os.scandir(ytdPath):
       if file.is_file():
           temp = str(file)
           endingIndex = temp.find('Income Statement') - 1
           trimmedName = temp[11:endingIndex]
           destination = dest_dir + '/' + trimmedName
           if os.path.exists(destination):
                shutil.copy(file, destination)
           else:
                os.makedirs(dest_dir + '/' + trimmedName)
                shutil.copy(file, dest_dir + '/' + trimmedName)
               
def RentRoll():
    dest_dir = MonthYearFormat() + '/Property Folders'

    for file in os.scandir(rentRollPath):
       if file.is_file():
           temp = str(file)
           endingIndex = temp.find('Rent Roll') - 1
           trimmedName = temp[11:endingIndex]
           destination = dest_dir + '/' + trimmedName
           if os.path.exists(destination):
                shutil.copy(file, destination)
           else:
                os.makedirs(dest_dir + '/' + trimmedName)
                shutil.copy(file, dest_dir + '/' + trimmedName)


def CreateInvestorFoldersWithPropertyStatements():
    root_dir = MonthYearFormat() + '/Investor Folders'

    for folder in os.scandir(MonthYearFormat() + '/Property Folders'):
        investorNames = propertyKeyDictionary.get(folder.name)
        if investorNames != None:  
            for i in investorNames:
                try: 
                    os.makedirs(str(root_dir) + '/' + i)
                    shutil.copytree(MonthYearFormat() + '/Property Folders/' + folder.name, MonthYearFormat() + '/Investor Folders/' + i + '/' + folder.name)
                except FileExistsError:
                    print(folder.name + ' Directory Exists')
                    
                
                


CreateInvestorPropertyDictionary()
CreatePropertyFolders()
BalanceSheet()
IncomeStatement()
RentRoll()
CreateInvestorFoldersWithPropertyStatements()


