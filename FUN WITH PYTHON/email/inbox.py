import imaplib
import email

host = 'imap.gmail.com'
username = 'abhaypy3@gmail.com'
password = 'Benayangla'

mail = imaplib.IMAP4_SSL(host)
mail.login(username,password)
mail.select("inbox")
_, search_data = mail.search(None,'UNSEEN')

for num in search_data[0].split():
    _, data = mail.fetch(num,'(RFC822)')
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    print(email_message)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
            body = part.get_payload(decode = True)
            print(body)

#print(search_data)