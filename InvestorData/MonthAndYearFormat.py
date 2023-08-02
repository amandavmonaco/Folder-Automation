from datetime import date

currentDate = date.today()
monthAndYear = str(currentDate)[0:7]
month = str(currentDate)[5:7]
year = str(currentDate)[0:4]

def MonthYearFormat():
    monthYear = month + '.' + year
    return monthYear



