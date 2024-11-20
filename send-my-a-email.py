import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email():
    # E-Mail-Details
    sender_address = ''
    sender_pass = os.environ.get("EMAIL_PASSWORD")
    receiver_address = ''

    # Setup der MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Arbeitszeit Log dieser Woche'   # Der Betreff der E-Mail

    # Dateipfad der Log-Datei
    file_path = os.path.expanduser("~\\Desktop\\time_tracker_log.txt")

    # Anhang hinzufügen
    attachment = open(file_path, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(file_path))
    message.attach(p)

    # SMTP-Sitzung erstellen und E-Mail senden
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)  # Der SMTP-Server und Port
        server.starttls()  # Die Sicherheit der Verbindung erhöhen
        server.login(message['From'], sender_pass)
        server.sendmail(message['From'], message['To'], message.as_string())
        server.quit()
        print("E-Mail erfolgreich gesendet.")
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail: {e}")

# Funktion aufrufen, um die E-Mail beim Herunterfahren des Rechners zu senden
send_email()
