from django.core.management.base import BaseCommand

from search.models import Product


class Command(BaseCommand):
    help = "Clear database "

    def handle(self, *args, **options):
        try:
            Product.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Suppression des données de la table "Product" : OK'))
        
        except Exception as e:
            self.stderr.write(self.style.ERROR('Erreur lors de la suppression des données de la table "Product"'))
