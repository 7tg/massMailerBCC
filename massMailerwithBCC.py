import smtplib
import csv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
import sys

import MainForm as Ui_MainWindow



##Function for reading user info from csv file
def readUserFile(csv_filename = None):
    try:
        with open(csv_filename, 'rb') as csvfile:
            file = {}
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                file[row[0]] = row[1]
        return file
    except Exception:
        raise Exception("CSV File not found")

##Function for reading HTML file
def readHTML(html_file = None):
    try:
        with open(html_file, 'r') as html_file_pt:
            return html_file_pt.read()
    except Exception:
        raise Exception("HTML File not found")

##Function for creating mail instance
def createMail(fromaddr = None,toaddr = None,subject = None,body = None):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = str(subject)
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg.attach(MIMEText(body, 'html'))
    return msg

##Function for login
def login(username=None, password=None):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    return server

##Function for logout
def logout(login):
    login.quit()



##Function for sendig mail from list of mail
def sendMailFromFile(mail_list_file = None,user = None,login = None,html = None,Ui_MainWindow = None):
    row_count = 0

    ##Reading mail list

    with open(mail_list_file,"r") as mail_list_file_pt:
        ##Counting rows

        for row_count, l in enumerate(mail_list_file_pt):
            pass
        row_count += 1
        bcc_count = int(user['bcc'])
        Ui_MainWindow.progressBar.setValue(0)

        ##Resetting file pointer
        mail_list_file_pt.seek(0,0)

        msg = createMail(user['username'], ' ', user['subject'], html)

        bcc_mails = ['']
        backup_i = 0
        for i in range(0,row_count):
            backup_i += 1


            ##Reading mails line by line
            mail = mail_list_file_pt.readline()
            ##Waiting for a interval
            bcc_mails.append(mail)
            bcc_count -= 1
            ##Sending mail
            if bcc_count == 0 or i == (row_count-1):
                if sendMail(login,user['username'],bcc_mails,msg.as_string()):
                    bar = (backup_i * 100) / row_count
                    if bar > 100 or bar < 0:
                        Ui_MainWindow.progressBar.setValue(100)
                    Ui_MainWindow.progressBar.setValue(bar)
                    Ui_MainWindow.lcdMail.display(backup_i)
                    for i in bcc_mails:
                        Ui_MainWindow.mail_text(i)
                    Ui_MainWindow.Mail_Label.scrollToBottom()
                    bcc_mails[:] = []
                    bcc_count = int(user['bcc'])
                    Ui_MainWindow.wait(int(user['timeInterval']))
                ##If returns false program shuts
                else:
                    mail_list_file_pt.close()
                    return False

    mail_list_file_pt.close()
    return True

##Main function for sending mail
def sendMail(server = None,fromaddr = None,toBCC = None,text = None):
    ##Exception handling
    if text == None:
        raise SystemError("msg doestn't exist")
        return False
    elif toBCC == None:
        raise SystemError("toBCC doestn't exist")
        return False
    elif server == None:
        raise SystemError("server doestn't exist")
        return False
    try:
        server.sendmail(fromaddr,toBCC, text)
        return True
    except Exception:
        return False



