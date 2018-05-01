# Project Title

This is a Python2 application for sending bulk mail lists with bcc.

## Getting Started

You can use either use GUI in qt folder or mainForBCC.py. The program supports only GMail for now and you have to edit your account settings from [Link](https://myaccount.google.com/lesssecureapps) before using the app. 

### Prerequisites

```
-PyQt4(4.11.4)
-csv
-email
-time
-sys
-smtplib
```

## Running

Mail list need to be in mail.txt in order to use GUI, and there is also USERFILE.csv that you need to edit before running the app.
The mail you want to send need to be in html format, you can edit html_file.html.

Example USERFILE
'''
username,example@example.com
password,yourPasswordHere
subject,mailSubjectHere
timeInterval,10 //Interval for program to wait
bcc,40 // You can add at most 80 BCC in a single mail
'''

Example mail.txt
'''
example@exapmle.com
example@exapmle.com
example@exapmle.com
example@exapmle.com
'''

## Built With

* [Python2](https://www.python.org)
* [PyQt4](https://pypi.org/project/PyQt4/) - For GUI purposes



## Authors

* **Tayyip Gören** - [tayyipgoren](https://github.com/tayyipgoren)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details