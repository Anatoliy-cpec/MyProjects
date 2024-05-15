from .models import Post, Subscribers


from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import datetime


@shared_task
def weekly_posts_task():

    today = datetime.datetime.now()

    last_week = today - datetime.timedelta(days=7)

    posts = Post.objects.filter(creation_date__gte=last_week)

    categories = set(posts.values_list('category', flat=True))
    
    subscribers = set(Subscribers.objects.filter(category__in=categories).values_list('user__email', flat=True))
    
    print(subscribers)
    print(posts)

    html_content = render_to_string(
        'daily_post.html',
        {
            'link' : f'http://127.0.0.1:8000',
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Weekly posts',
        body='',
        from_email=None,
        to=subscribers,
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

@shared_task
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
