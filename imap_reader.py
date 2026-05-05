import imaplib
import email
import os

EMAIL = "kowshik8125@gmail.com"
APP_PASSWORD = "tvsrslqcyzehyefl"

# SAVE_PATH = r"C:\Users\BOSON-177\Desktop\new_project\PDF_Generator\sample_pdfs"
SAVE_PATH = "temp_pdfs"


def fetch_attachments():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")

    os.makedirs(SAVE_PATH, exist_ok=True)

    saved_files = []

    for num in messages[0].split()[-10:]:
        status, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        for part in msg.walk():
            if part.get_content_type() == "application/pdf":
                filename = part.get_filename() or f"file_{num}.pdf"
                if filename:
                    filepath = os.path.join(SAVE_PATH, filename)

                    if os.path.exists(filepath):
                        continue

                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))

                    saved_files.append(filepath)

    mail.logout()
    return saved_files