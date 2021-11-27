import os
import sys
from datetime import datetime

proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

import django
django.setup()
 
from django.core.mail import EmailMultiAlternatives
from core.settings import EMAIL_HOST_USER
from jobs.models import Follower, Xamerz

posts = Xamerz

emails = Follower.objects.all()

subject = f'Новости на сегодня {datetime.today()}'
from_email = EMAIL_HOST_USER
text_content = 'Рассылка новостей!'
html_content = '' 
for post in posts:
        html_content += f'''<h3 class="card-title">{ post.get('title') }</h3>
                <p class="card-text">{ post.get('tag') } | { post.get('rate') } | {post.get('date')}</p>
                <h6 class="card-title">{ post.get('time') }</h6>
                <a href="{post.get('url')}" class="btn btn-primary">Перейти к новости</a><br>'''
msg = EmailMultiAlternatives(subject, text_content, from_email, email=emails)
msg.attach_alternative(html_content, "text/html")
msg.send()