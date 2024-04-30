import smtplib
import ssl


def send_mail(sender_mail, message):
    host_name = "emailexperimental70@gmail.com"
    password = "skxvm byun scdk igak"
    host = "smtp.email.com"
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(host_name, password)
        server.sendmail(sender_mail, host_name, message)


