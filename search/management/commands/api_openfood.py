from django.core.management.base import BaseCommand
import requests
import json


class Command(BaseCommand):
    help = "Custom command"

    def handle(self, *args, **options):
        url = 'https://world.openfoodfacts.net/api/v2/product/3017620422003'
        request = requests.get(url)
        self.stdout.write(self.style.SUCCESS(json.dumps(request.json(), indent=4)))
