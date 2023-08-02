from datetime import date

currentDate = date.today()
monthAndYear = str(currentDate)[0:7]
month = str(currentDate)[5:7]
year = str(currentDate)[0:4]

textMonth = ''

if month == '01':
    textMonth = 'January'

if month == '02':
    textMonth = 'February'

if month == '03':
    textMonth = 'March'

if month == '04':
    textMonth = 'April'

if month == '05':
    textMonth = 'May'

if month == '06':
    textMonth = 'June'

if month == '07':
    textMonth = 'July'

if month == '08':
    textMonth = 'August'

if month == '09':
    textMonth = 'September'

if month == '10':
    textMonth = 'October'

if month == '11':
    textMonth = 'November'

if month == '12':
    textMonth = 'December'


def MonthYearFormat():
    monthYear = month + '.' + year
    return monthYear



