from django.core.management.base import BaseCommand, CommandError
from accounts.models import Domains

class Command(BaseCommand):
    args = 'None'
    help = 'Gets all the domains'

    def handle(self, *args, **options):
        domains = Domains.objects.all()
        for domain in domains:
            self.stdout.write('*.%s\n' % domain.domain)
