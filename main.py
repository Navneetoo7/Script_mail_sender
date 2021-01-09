import smtplib
from smtplib import SMTPException

s = smtplib.SMTP('smtp.gmail.com',587)
sender = '**********@gmail.com'
receivers = '********@gmail.com'
s.starttls()
s.login(sender,"*******")
message = '********number'
s.sendmail(sender, receivers, message)
s.quit()
try:
   s = smtplib.SMTP('localhost')
   s.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")