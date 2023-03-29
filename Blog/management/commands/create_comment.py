import random

from Blog.models import Comments, Posts

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('create_comment', nargs='?',
                            help='Create a random comment')

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(500):

            Comments.objects.create(comment=''.join(fake.paragraphs()),
                                    post=Posts.objects.get(pk=random.randint(1, 50)),
                                    author=random.choice([
                                        'AnonymousUser',
                                        User.objects.get(pk=random.randint(1, 20))]),
                                    is_published=random.choice([True, False])
                                    )
