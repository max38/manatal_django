import random
from django.core.management.base import BaseCommand
from faker import Faker
from school.models import School, Student
from school.enum import SexEnum, NationalityEnum


class Command(BaseCommand):
    help = 'Initial Fake Data'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        number = options['number']

        fake = Faker()

        school = School.objects.create(
            name=fake.company(),
        )

        i = 0
        while i < number:
            try:
                student = Student.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    sex=random.choice(SexEnum.value_list()),
                    nationality=random.choice(NationalityEnum.value_list()),
                    school=school
                )
                print("{} : {} {}".format(student.id, student.first_name, student.last_name))
                i += 1
            except:
                continue
