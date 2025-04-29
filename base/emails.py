from django.conf import settings
from django.core.mail import send_mail , EmailMessage

def send_account_activation_email( email , email_token):

    subject = 'Verify Your Account'
    activation_link = f"http://127.0.0.1:8000/accounts/verify/{email_token}/"
    message = f'''
    <div style="font-family: Arial, sans-serif; color: #333;">

        <h2>Welcome!</h2>
        <p>Thanks for signing up. Please click the button below to verify your email address and activate your account:</p>
        <p style="text-align: center; margin: 20px 0;">
            <a href="{activation_link}"
                style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                Verify My Account</a>
        </p>
        <p>If the button doesn't work, click the link below:</p>
        <p><a href="{activation_link}">{activation_link}</a></p>
        <br>
        <p>— Your Website Team</p>
    </div>
    '''

    email_from = settings.EMAIL_HOST_USER

    recipient_list = [email]


    email_message = EmailMessage( subject , message , email_from, recipient_list)
    email_message.content_subtype = "html"
    email_message.send()