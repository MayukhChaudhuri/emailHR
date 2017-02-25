import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def sendEmail(toaddr, jobID, pos):  
    fromaddr = "abc@xyz.com"   #your email ID using which you want to send the emails
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Follow up"

    if jobID == None and pos is not None:
        body = "Hi,\nMy name is XYZ.\nThis is a follow up email sent by my python script.\nI have applied at your company for the following position(s): "+pos+"\nI have attached my resume for easy reference.\nSincerely,\nMayukh"
    elif jobID is not None and pos is None:
        body = "Hi,\nMy name is XYZ.\nThis is a follow up email sent by my python script.\nI have applied at your company for the following job(s): "+jobID+"\nI have attached my resume for easy reference.\nSincerely,\nMayukh"
    elif jobID is not None and pos is not None:
        body = "Hi,\nMy name is XYZ.\nThis is a follow up email sent by my python script.\nI have applied at your company for the following position(s): "+pos+"("+jobID+")"+"\nI have attached my resume for easy reference.\nSincerely,\nMayukh"
    elif jobID is None and pos is None:
        body = "Hi,\nMy name is XYZ.\nThis is a follow up email sent by my python script.\nI have attached my resume for easy reference.\nSincerely,\nMayukh"

    msg.attach(MIMEText(body, 'plain'))
     
    filename = "Resume.pdf"
    attachment = open("PATH TO YOUR RESUME WHICH YOU WANT TO SEND WITH THE EMAIL", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "PASSWORD OF YOUR EMAIL ACCOUNT USING WHICH YOU WANT TO SEND THE EMAILS")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print 'email sent'
