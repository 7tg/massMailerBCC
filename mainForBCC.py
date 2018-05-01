import  massMailerwithBCC as mail

##Read user info ftom user.csv
user = mail.readUserFile("userForBCC.csv")

##Read mail form HTML file
html = mail.readHTML("html_file.html")

##Create instance of mail
msg = mail.createMail(user['username'],user['username'],user['subject'],html)

##Login with user info
login = mail.login(user['username'], user['password'])

##Main function
mail.sendMailFromFile("mailler.txt",user,login,html)

##Log out
mail.logout(login)



