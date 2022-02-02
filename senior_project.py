import smtplib
from email.message import EmailMessage

def send_email():   # I think I have to add the reciver, subject and content message at here
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('chongfanding@gmail.com', 'Yyf19960102.')
    email = EmailMessage()
    email['From'] = 'chongfanding@gmail.com'
    email['To'] = 'Chris.liu@gmail.com'
    email['Subject'] = 'Can you help me with my tax'
    email.set_content('Hi Chris, can you help me? Thank you')
    server.send_message(email)
    # server.sendmail('chongfanding@gmail.com',
    #                 'chongfanding@gmail.com',
    #                 'Hello from myself')
    # you have to turn on google account -> security -> less secure app access -> on