import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("dasarikhada@gmail.com","password")
subject="test python"
body="i love python"
massage="subject:{}\n\n{}". format(subject,body)
listadd=["dasarikhada@gmail.com"]
ob.sendmail("dasarikhada@gmail.com",listadd,massage)
print("Send mail")
ob.quit
