from django.core.mail import send_mail
from django.conf import settings

def send_email_to_candidate(candidate, template):
    send_mail(
        subject=template.title,
        message=template.content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[candidate.email],
        fail_silently=False,
    )
