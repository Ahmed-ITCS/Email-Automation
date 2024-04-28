import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_paths):
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach body
    msg.attach(MIMEText(body, 'plain'))

    # Attach images
    for attachment_path in attachment_paths:
        with open(attachment_path, 'rb') as attachment_file:
            img_part = MIMEImage(attachment_file.read())
            img_part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            msg.attach(img_part)

    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close connection
    server.quit()

# List of email addresses
email_list = ['ahmedkhawar.80@gmail.com']

'''["zaeem@developers.studio",
"iram.ijaz@developers.studio",
"Mubashra.bashir@purelogics.net", 
"careers@nextbridge.com",
"careers@citrok.com",
"Qiran.sohail@intersoftbpo.com",
"arisha.atif@manafatech.com",
"suman.shahzad@thetowertech.com",
"zirva@whiteboxtech.net",
"muhammad.usman@piecyfer.com",
"operations.hr@magnatecsystems.com",
"careers@hazentech.com",
"careers@invozone.com",
"hr@mentorsol.com",
"hr@innovadeltech.com"]'''

# Sender email credentials
sender_email = 'ahmedkhawarbs@gmail.com'
sender_password = 'cgtj zvww yhbs vvgu'

# Email details
subject = "Handing out my CV"
body = "I trust this message finds you well.\nI am emailing in the light of recent discussion we had over at UCP carrer fair this friday and you told me to forward you my resume. Please find my resume attached to this email.\n\nA little introduction about me:\nI am Software engineering last semester student graduting in the month of July. I am a active freelancer, I usally work in with backend technologies like Django and Laravel and for the front end I use React.js, also make use of different version control systems like bit bucket or github.\nI have also served as intern in Vertex IT services"

# List of attachment file paths
attachment_paths = ['AhmedKhawarSoftwareengineer.pdf']

# Iterate through the email list and send emails
for receiver_email in email_list:
    send_email(sender_email, sender_password, receiver_email, subject, body, attachment_paths)
    print("\n Email sent to ",receiver_email)

print("Emails sent successfully.")
