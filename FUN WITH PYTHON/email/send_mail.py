import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'abhaypy3@gmail.com'
password = 'Benayangla'

def send_mail(text = 'Email Body',subject = 'Hello world',from_email = 'ABHAY KUMAR <abhaypy3@gmail.com>',to_emails=['abhaynitn@gmail.com','abhaykumar912244@gmail.com','nitnabhay@gmail.com']):
    assert (isinstance(to_emails,list))
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)

    html_part = MIMEText("""
<!DOCTYPE html>
<html>
<head>
<title>Font Awesome Icons</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
<!--Get your own code at fontawesome.com-->
</head>
<body>

<h1>Font Awesome icon library</h1>

<p>Some Font Awesome icons:</p>
<i class="fas fa-cloud"></i>
<i class="fas fa-heart"></i>
<i class="fas fa-car"></i>
<i class="fas fa-file"></i>
<i class="fas fa-bars"></i>

<p>Styled Font Awesome icons (size and color):</p>
<i class="fas fa-cloud" style="font-size:24px;"></i>
<i class="fas fa-cloud" style="font-size:36px;"></i>
<i class="fas fa-cloud" style="font-size:48px;color:red;"></i>
<i class="fas fa-cloud" style="font-size:60px;color:lightblue;"></i>

</body>
</html>



""",'html')
    msg.attach(html_part)

    msg_str = msg.as_string()
    #login to my smtp server
    server = smtplib.SMTP(host = 'smtp.gmail.com',port = 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()

    #with smtplib.SMTP() as server:
    #    server.login()
    #    pass
send_mail()