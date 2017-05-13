from email.mime.text import MIMEText
import smtplib


def send_email(email,height,average_height,count):
    from_email="aakashmhankale@gmail.com"
    from_password="Lifeisgood123!"
    to_email=email

    subject="Height Data"
    message="Hey Hi,Your height is <strong>%s</strong>. Average height of all users till now is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people." %(height,average_height,count)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.ehlo()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
