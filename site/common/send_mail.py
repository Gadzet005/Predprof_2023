import smtplib


def send_mail(text):
    server = smtplib.SMTP_SSL('smtp.mail.ru:465')
    server.login('e.kulpin@mail.ru', 'uncNCJmQSC7aKTSvwxMz')
    server.sendmail('e.kulpin@mail.ru', 'ea.kulpin@mail.ru', text)
    server.quit()
