from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='moder@admin.com',
            first_name='Moder',
            last_name='Moderatov',
            is_staff=True,
            is_superuser=False,
        )

        user.set_password('moder12345')
        user.groups.add(1)
        user.save()
