import csv
from django.core.management.base import BaseCommand
from ads_miniproject.models import StockMarketNews

class Command(BaseCommand):
    help = 'Import stock market news from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StockMarketNews.objects.create(
                    source=row['source'],
                    headline=row['headline'],
                    url=row['url'],
                    content=row['content'],
                    image=row['image']
                )
        self.stdout.write(self.style.SUCCESS('Stock market news imported successfully'))
