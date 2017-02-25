import  openpyxl, time, emailHR
from datetime import datetime

def readExcel():
    wb = openpyxl.load_workbook('Internship applications.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    Irows = []
    for i in sheet['I']:
        if i.value == 'Followup Date':
            continue
        if i.value == None:
            Irows.append(i.row)
    i = 0
    while i<len(Irows):
        if sheet['D'+str(Irows[i])].value=='Rejected':
            del Irows[i]
            i = i - 1
        i = i + 1
        
    for i in sheet['H']:
        if i.row not in Irows or i.value == None :
            continue
        if sheet['J'+str(i.row)].value == None:
            print '\nemailID not present for row number : ',i.row,'\n'
            continue
        today = datetime.strptime(datetime.today().strftime('%m-%d-%Y'), '%m-%d-%Y')
        date = str(i.value.month)+"-"+str(i.value.day)+"-"+str(i.value.year)
        convDate = datetime.strptime(date, '%m-%d-%Y')
        if int(str(today - convDate).split(" ")[0])>=21:
            toaddr = sheet['J'+str(i.row)].value
            jobID =  sheet['B'+str(i.row)].value
            pos = sheet['C'+str(i.row)].value
            if jobID is None or pos is None:
                print 'Job ID and/or position details missing for row number : ',i.row,'\n'
            emailHR.sendEmail(toaddr, jobID, pos)
            print "email sent for ",sheet['J'+str(i.row)].value
            sheet['I'+str(i.row)] = time.strftime("%c")
            wb.save('Internship applications.xlsx')

def main():
    readExcel()
    
if __name__ == '__main__':
    main()
