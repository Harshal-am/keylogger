import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "animelover05022004@gmail.com"
    password = "vslb ggpo yode dxul"
    receiver_email = "animelover05022004@gmail.co"

    # Check if message is None or empty
    if message is None or message.strip() == "":
        print("Error: message is None or empty")
        return  # Early exit to prevent sending empty or None messages

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted, but helps with server identification
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Again, helps with server communication
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode())  # Ensure message is encoded
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred while sending email: {e}")
    finally:
        server.quit()