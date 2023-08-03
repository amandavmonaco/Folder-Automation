import os 
import shutil
import pandas as pd
from MonthAndYearFormat import *

propertyKeyDictionary = {}
monthYear = MonthYearFormat()

#  These variables hold the names of the folders the financial statements are located in. The folder names must match exactly to these variables.
#  These folders must also be located in the current working directory (where this program's files are located). If they aren't, you can change this path
#  to a different format (e.g. '/Users/amandamonaco/Documents/Bal Sheet')
balanceSheetsPath = 'Bal Sheet'
rentRollPath = 'Rent Roll'
IncomeStatementPath = 'YTD'

#  This function will read in the provided excel file. The excel file must be named 'InvestorPropertiesPyFile' and also exist in the current working
#  directory. If the file is incorrectly named or does not exist in the correct directory then there will be a statement printed to the terminal
def CreateInvestorPropertyDictionary():
    try:
        excelFile = pd.read_excel('InvestorPropertiesPyFile.xlsx') 
    except FileNotFoundError:
        print('Investor Properties File was not found')

    for column in excelFile:
        column_values = excelFile[column].tolist()
        filtered_values = [value for value in column_values if not pd.isnull(value)]
        propertyKeyDictionary[column] = filtered_values


#  This is a test function and does not need to be called to make the program run
def TestFunctionToPrintDictionary():
    for propertyKey in propertyKeyDictionary.keys():
        print('KEY: ' + propertyKey)
        for investors in propertyKeyDictionary[propertyKey]:
            print(' INVESTOR: ' + investors)


#  This function creates a folder named 'Property Folders' within the month.year folder. This folder will contain folders for all current properties
#  with their balance sheet, rent roll, and income statement in them. The purpose is to be able to access any property's financial statements at any point
def CreatePropertyFolders():
    root_dir = monthYear + '/Property Folders'

    for property in propertyKeyDictionary.keys():
        folderName = str(root_dir) + '/' + str(property)
        try: 
            os.makedirs(folderName)
        except:
            print(property + ' Directory Exists')

#  The following three functions pull the documents from the provided folders and place them into each property folder
def BalanceSheet():
   dest_dir = monthYear + '/Property Folders'

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
   dest_dir = monthYear + '/Property Folders'

   for file in os.scandir(IncomeStatementPath):
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
    dest_dir = monthYear + '/Property Folders' 

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


#  This function will create folders for each Investor within a the month.year folder and under another folder named 'Investor Folders'. Each Investor
#  will have a folder for the properties they are listed under within the provided excel file. If the property is a commercial property or has been sold
#  but has not been removed from the excel sheet, there will be an empty folder named with the title of the property.
def CreateInvestorFoldersWithPropertyStatements():
    root_dir = monthYear + '/Investor Folders'

    for folder in os.scandir(MonthYearFormat() + '/Property Folders'):
        investorNames = propertyKeyDictionary.get(folder.name)
        if investorNames != None:  
            for i in investorNames:
                try: 
                    os.makedirs(str(root_dir) + '/' + i)
                except FileExistsError:
                    print(folder.name + ' Directory Exists')
                shutil.copytree(MonthYearFormat() + '/Property Folders/' + folder.name, 
                                MonthYearFormat() + '/Investor Folders/' + i + '/' + folder.name,
                                dirs_exist_ok=True)

#Calling the functions: 
CreateInvestorPropertyDictionary()
CreatePropertyFolders()
BalanceSheet()
IncomeStatement()
RentRoll()
CreateInvestorFoldersWithPropertyStatements()


