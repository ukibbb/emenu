from datetime import timedelta

from accounts.models import User
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.utils.timezone import now
from menu_items.models import MenuItem


@shared_task
def notify_users_about_last_created_and_updated_items():
    """
    Sends email for each user with notification about recently created
    and updated dishes in our menus.
    """
    subject = "New added and last modified dishes from our menus."
    today = now()
    yesterday = today - timedelta(days=1)

    created_within_one_day = MenuItem.objects.filter(
        created_at__gte=yesterday, created_at__lte=today
    )
    updated_within_one_day = MenuItem.objects.filter(
        updated_at__gte=yesterday, updated_at__lte=today
    )

    message = "Hey! This is what's new in our menu."

    recipient_list = [user.email for user in User.objects.all()]

    html_message = loader.render_to_string(
        "notify_users.html",
        {"updated": updated_within_one_day, "created": created_within_one_day},
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_FROM,
        recipient_list=recipient_list,
        html_message=html_message,
        fail_silently=False,
    )
