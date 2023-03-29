import random

from Blog.models import Posts

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('create_post', nargs="?",
                            help='Create random posts')

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(50):
            subject = []
            text = []
            for _ in range(3):
                subject += fake.word()
                text += fake.paragraphs()
            Posts.objects.create(subject=''.join(subject),
                                 synopsis=fake.paragraphs()[0],
                                 text=" ".join(text),
                                 is_published=random.choice([True, False]),
                                 owner=User.objects.get(pk=random.randint(1, 20))
                                 )
