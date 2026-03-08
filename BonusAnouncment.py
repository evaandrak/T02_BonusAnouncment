import csv

class Employee:
    EmployeeId = ''
    FullName = ''
    BonusAmount = 0
    HasPromotion = True

EmployeeObjectsList = []

csvfilename = '/home/eva/code/T02_BonusAnouncment/employees_bonus_dataset.csv'
EmailFolderPath = '/home/eva/Email/'
EmailText = 'Dear #name# we are happy to announce that you will receive a bonus of #number# CHF.'

PromationText = ' We are also proud to to inform you that you are promoted. Congratulations!'


with open(csvfilename, newline='') as csvfile:
    EmployeeReader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in EmployeeReader:
        EmployeeData = Employee()
        EmployeeData.EmployeeId = row[0]
        EmployeeData.FullName = row[1]
        EmployeeData.BonusAmount = row[2]
        EmployeeData.HasPromotion= row[3]
        EmployeeObjectsList.append(EmployeeData)

for e in EmployeeObjectsList:
    EmployeeTxt = EmailText.replace('#name#',e.FullName)
    EmployeeTxt = EmployeeTxt.replace('#number#',str(e.BonusAmount))
    if e.HasPromotion == '1':
        EmployeeTxt = EmployeeTxt + PromationText
    # print(EmployeeTxt)
    FileEmail = EmailFolderPath + e.EmployeeId + '.txt'
    with open(FileEmail,'w') as tf:
        tf.write(EmployeeTxt)

print('finished')