from django.core.management.base import BaseCommand, CommandError

from subjects.models import Subject


class Command(BaseCommand):
    help = 'Show average mark per subject'

    def handle(self, *args, **options):
        subjects = Subject.objects.all()
        for subject in subjects:
            total_marks = 0
            counter = 0
            for enrollment in subject.enrollments.all():
                if enrollment.mark is not None:
                    total_marks += enrollment.mark
                    counter += 1
            if counter == 0:
                self.stdout.write(f'{subject.code}: 0.00')
            else:
                self.stdout.write(f'{subject.code}: {(total_marks / counter):.2f}')