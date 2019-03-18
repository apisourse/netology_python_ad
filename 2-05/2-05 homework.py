import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
Создать класс для работы с почтой;
Создать методы для отправки и получения писем;
Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
Переменные должны быть названы по стандарту PEP8;
Весь остальной код должен соответствовать стандарту PEP8;
Класс должен инициализироваться в конструкции.
"""

SERVER_SMTP = "smtp.yandex.com"
SERVER_IMAP = "imap.yandex.com"
SERVER_PORT = "465"


class SendMail():

    def __init__(self, SERVER_SMTP, SERVER_IMAP, SERVER_PORT):

        self.SERVER_SMTP = SERVER_SMTP
        self.SERVER_IMAP = SERVER_IMAP
        self.SERVER_PORT = SERVER_PORT

    def send_message(self, login, password,
                     recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        try:
            smtp_server = smtplib.SMTP(self.SERVER_SMTP, self.SERVER_PORT)  # identify ourselves to smtp gmail client
            smtp_server.set_debuglevel(True)
            smtp_server.ehlo()  # secure our email with tls encryption
            smtp_server.starttls()  # re-identify ourselves as an encrypted connection
            smtp_server.ehlo()
            smtp_server.login(login, password)
            smtp_server.sendmail(login, smtp_server, msg.as_string())
            smtp_server.quit()
            return 'successfully sent the mail'
        except Exception as e:
            raise e
            return "failed to send mail: {}".format(e)
        print('Все успешно')

    def get_message_inbox(self, login, password,
                          header=None, format_post_message):
        mail = imaplib.IMAP4_SSL(SERVER_IMAP)
        mail.login(login, password)
        mail.list()
        mail.select("inbox")

        criterion = '(HEADER Subject {})'.format(header) if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, format_post_message)
        raw_email = data[0][1]

        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message.items()


login = 'test@yandex.ru'
password = 'test'
recipients = ['test@gmail.com', 'test@yandex.ru']
subject = 'Some_Subject'
message = 'Some Message'

mail = SendMail(SERVER_SMTP, SERVER_IMAP, SERVER_PORT)

print(mail.send_message(login, password, recipients, subject, message))

header = 'Yandex'
format_post_message = '(RFC822)'
print(mail.get_message_inbox(login, password, header, format_post_message))
