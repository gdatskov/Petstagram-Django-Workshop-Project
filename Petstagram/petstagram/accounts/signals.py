from smtplib import SMTPNotSupportedError

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_signup(instance, created, **kwargs):
    if not created:
        return
    try:
        send_mail(
            subject='Registration to Petstagram',
            message='You have successfully registered on Petstagram',
            from_email=None,    # None = Use default
            recipient_list=(instance.email,),
        )
    except Exception as error:
        print(f'Cannot send the e-mail: \n{error}')

