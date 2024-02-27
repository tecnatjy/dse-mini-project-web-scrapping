import csv
from django.core.management.base import BaseCommand
from ads_miniproject.models import HistoricalData

class Command(BaseCommand):
    help = 'Import historical data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                HistoricalData.objects.create(
                    date=row['Date'],
                    open=row['Open'],
                    high=row['High'],
                    low=row['Low'],
                    close=row['Close'],
                    adj_close=row['Adj Close'],
                    volume=row['Volume']
                )
        self.stdout.write(self.style.SUCCESS('Historical data imported successfully'))
