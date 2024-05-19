from django.core.management import BaseCommand

from courses.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):

        Payment.objects.all().delete()
        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        User.objects.create(email='user1@email.com', password='123qwe456rty')
        User.objects.create(email='user2@email.com', password='123qwe456rty')
        Course.objects.create(name='Test', description='Testing')
        Lesson.objects.create(name='Test1', description='Testing1', course=Course.objects.get(name='Test'))
        Lesson.objects.create(name='Test2', description='Testing2', course=Course.objects.get(name='Test'))

        payment_list = [
            {
                'owner': User.objects.get(email='user1@email.com'),
                'date': '2024-04-20',
                'course': Course.objects.get(name='Test'),
                'lesson': Lesson.objects.get(name='Test1'),
                'price': '1000',
            },
            {
                'owner': User.objects.get(email='user2@email.com'),
                'date': '2024-05-20',
                'course': Course.objects.get(name='Test'),
                'lesson': Lesson.objects.get(name='Test2'),
                'price': '800',
            }
        ]

        payments = []

        for payment in payment_list:
            payments.append(Payment(**payment))

        Payment.objects.bulk_create(payments)
