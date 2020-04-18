# Общие настройки для отправки почты
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_TO_EMAIL = os.environ['DEFAULT_TO_EMAIL']   # адрес куда будут слаться письма
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # не важно для отправки.
# SERVER_EMAIL = EMAIL_HOST_USER        # не важно для отправкиэ


# Настройки почты mail.ru -----------------------------------------------------
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = os.environ['MAIL_EMAIL']
EMAIL_HOST_PASSWORD = os.environ['MAIL_PASSWORD']


# Настройки почты gmail.com ---------------------------------------------------
# Дополнительно для аккаунта google нужно разрешить работу с небезопасными приложениями:
# https://myaccount.google.com/lesssecureapps
# Если это не сделать, то будет ошибка:
# smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted.
# Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials z26sm6719526ljz.50 - gsmtp')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['GMAIL_EMAIL']
EMAIL_HOST_PASSWORD = os.environ['GMAIL_PASSWORD']


# Настройкий почты yandex.ru --------------------------------------------------
# При отправке с Яндекса сервер получателя может блокировать письмо как спам.
# Ошибка:
# smtplib.SMTPDataError: (554, b'5.7.1 [2]
# Message rejected under suspicion of SPAM;
# https://ya.cc/1IrBc 1587211628-x06xoxNCqI-782CkRfO')

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = os.environ['YANDEX_EMAIL']
EMAIL_HOST_PASSWORD = os.environ['YANDEX_PASSWORD']


В файле settings.py прописать константы (общие и конкретные для почтового сервера).
Установить переменные окружения.
В python manage.py shell запустить команды ниже:
from django.conf import settings
from django.core.mail import send_mail
send_mail('Subject here', 'Here is the message.',
          settings.EMAIL_HOST_USER, [settings.DEFAULT_TO_EMAIL], fail_silently=False,)
В ответе будет количество отправленных писем.
