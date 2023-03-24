from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_create', nargs='?',
                            help="Creates a random user with username, email. Password = 123.")

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(20):
            User.objects.create(username=fake.unique.user_name(),
                                           email=fake.unique.email(),
                                           password=make_password('123'),
                                last_name=fake.last_name(),
                                first_name=fake.first_name())
