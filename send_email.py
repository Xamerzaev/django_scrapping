import django
from django.core.mail import EmailMultiAlternatives
from core.settings import EMAIL_HOST_USER
from jobs.models import Follower
from scrapping import habr_parsing
import os
import sys
from datetime import datetime

proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

django.setup()

jobs = habr_parsing()
emails = Follower.objects.all()
subject = f'Новости на сегодня {datetime.today()}'
from_email = EMAIL_HOST_USER
text_content = 'Рассылка новостей!'
html_content = ''
for email in emails:
    for job in jobs:
        html_content += f'''<h3 class="card-title">{ job.get('title') }</h3>
                        <p class="card-text">{
                                job.get('tag') } | {
                                job.get('rate') } | {
                                job.get('date')}</p>
                        <h6 class="card-title">{ job.get('time') }</h6>
                        <a href="{job.get('url')}"\
                        class="btn btn-primary">Перейти к новости</a><br>'''
msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
msg.attach_alternative(html_content, "text/html")
msg.send()
