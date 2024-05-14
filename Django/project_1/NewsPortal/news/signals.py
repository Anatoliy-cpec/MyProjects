from .models import Subscribers, User

from django.db.models.signals import m2m_changed
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.dispatch import receiver


from .models import PostCategory

def send_notification(preview, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text' : preview,
            'link' : f'http://127.0.0.1:8000/posts/{pk}',
            'title' : title,

        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body=html_context,
        from_email=None,
        to=subscribers,
    )

    msg.attach_alternative(html_context, "text/html")
    msg.send()

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        
        categories = set(instance.category.all())

        subscribers = set(Subscribers.objects.filter(category__in=categories).values_list('user__email', flat=True))
        

        send_notification(instance.preview(), instance.id, instance.post_header, subscribers)


    