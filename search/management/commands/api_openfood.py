import json
import requests

from django.core.management.base import BaseCommand

from search.models import Product


class Command(BaseCommand):
    help = "Get Products"

    def handle(self, *args, **options):
        list_categories = ['chocolates', 'cheeses', 'sodas']

        for category in list_categories:
            url = f'https://world.openfoodfacts.net/api/v2/search?categories_tags_en={category}&fields=product_name,nutriscore_data,categories_tags,nutriscore_data'
            request = requests.get(url)
            liste_API_products = request.json()['products']

            for api_product in liste_API_products:
                if "nutriscore_data" in api_product:
                    product = Product(
                        name=api_product["product_name"],
                        nutri_score=api_product["nutriscore_data"]["grade"],
                        )
                    product.save()

                self.stdout.write(self.style.SUCCESS(f'  Enregistrement du produit {api_product["product_name"]} : OK'))
            
        self.stdout.write(self.style.SUCCESS('Enregistrement des produits dans la Base de données : OK'))
