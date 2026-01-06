from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'PLACEHOLDER'

    # def add_arguments(self, parser):
    #     parser.add_argument('post_pks', nargs='+', type=int)

    def handle(self, *args, **options):
        print("Subject Stats:")