import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def sendMail(name, adress, body, image_number):
    email_user = 'feedbackfromcodecool@gmail.com'
    email_send = adress
    subject = name

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))

    filename = '/home/gergo/Desktop/feedback_generator/static/picture_with_string/{}.jpg'.format(image_number)
    attachment =open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'Feedbackfromcodecool11')
    server.sendmail(email_user, email_send, text)
    server.quit()