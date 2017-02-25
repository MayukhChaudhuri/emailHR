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
  
 In the EmailHR script:
 You will have to put your email ID and password using which you want the followup email to be sent.
 fromaddr = "abc@xyz.com"
 server.login(fromaddr, "PASSWORD OF YOUR EMAIL ACCOUNT USING WHICH YOU WANT TO SEND THE EMAILS")
 
 You will have to put your name in the code which is responsible for composing the body of the email.
 body = "Hi,\nMy name is XYZ.............."
 
 You will also have to enter the path of the resume which you want to send along with the followup emails.
 attachment = open("PATH TO YOUR RESUME WHICH YOU WANT TO SEND WITH THE EMAIL", "rb")
 
 You can change the filename being attached by editing the following line:
 filename = "Resume.pdf"
  
 In the Excel Sheet: 
 There has to be a column with the title "Followup Date".
 
 The status column can take only two values Under review/ Rejected.
