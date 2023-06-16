import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

log_file = "log.txt"

def encrypt_and_write_exception(exception):
    encrypted_exception = cipher_suite.encrypt(exception.encode())

    with open(log_file, "a") as file:
        file.write(encrypted_exception.decode() + "\n")

def send_encrypted_email(sender_email, sender_password, receiver_email, subject, message):
    encrypted_message = cipher_suite.encrypt(message.encode())

    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(encrypted_message.decode(), "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("Mail was sent with success.")
    except Exception as e:
        print("An error occurred while sending mail:", str(e))


try:
    x = 10 / 0
except Exception as e:
    encrypt_and_write_exception(str(e))

    sender_email = "sender@gmail.com"
    sender_password = "sender_password"
    receiver_email = "receiver@gmail.com"
    subject = "Error notification"
    message = str(e)

    send_encrypted_email(sender_email, sender_password, receiver_email, subject, message)
