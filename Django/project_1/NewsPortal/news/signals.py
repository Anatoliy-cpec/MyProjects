from .models import Subscribers
from .tasks import send_notification
from django.db.models.signals import m2m_changed

from django.dispatch import receiver


from .models import PostCategory



@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        
        categories = set(instance.category.all())

        subscribers = set(Subscribers.objects.filter(category__in=categories).values_list('user__email', flat=True))
        

        send_notification(instance.preview(), instance.id, instance.post_header, subscribers)


    