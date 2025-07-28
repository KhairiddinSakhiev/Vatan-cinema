from django.core.mail import send_mail
from django.conf import settings


def send_confirmation_token(email, token ):
    path = f'http//:127.0.0.1:8000/auth/confirm-email/{token}'
    message = f"""Hello. Someone used this email for registration in VATAN.tj platform.
Please confirm it's you by clicking ---> {path}"""
    
    try:
        send_mail(
            subject='VATAN.tj',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list= [email]
        )
        return {
            'is_sent' : True,
            'message' : 'Message sent successfully!'
        }
    except Exception as e:
        return {
            'is_sent' : False,
            message : str(e)
        }