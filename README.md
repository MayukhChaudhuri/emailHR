# emailHR

This application helps you to follow up with the hiring manager or the HR team after applying to jobs.

This application considers that you are maintaining a detailed record of all the positions he/she has applied to in an excel sheet.

The format of the excel sheet has been provided.

This application sends follow up emails only if you haven't heard back from the company in 3 weeks (21 days) after applying for the position. If you want to change this interval to 2 weeks (14 days) then you will have to change this following one line in the ReadingExcel.py file :
  if int(str(today - convDate).split(" ")[0])>=21 has to be changed to if int(str(today - convDate).split(" ")[0])>=14

If the format of the excel sheet that you are using is different from the one that has been provided here then you will have to make few minor changes to the ReadingExcel.py file depending on how different is the format of the excel sheet from the one that has been provided.

For eg :
In the excel sheet that has been provided here the column 'J' is 'HR email'.
If in the excel sheet you are using the column containing the email IDs is suppose 'K' then you would have to make changes like this:
  i) if sheet['J'+str(i.row)].value == None would become if sheet['K'+str(i.row)].value == None.
  ii) toaddr = sheet['J'+str(i.row)].value would become toaddr = sheet['K'+str(i.row)].value.
