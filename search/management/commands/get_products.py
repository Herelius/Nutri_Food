import requests
from django.core.management.base import BaseCommand

from search.models import Product


class Command(BaseCommand):
    help = "Get Products"

    def handle(self, *args, **options):
        all_products = []
        list_categories = ['chocolates', 'cheeses', 'sodas']

        for category in list_categories:
            url = f'https://world.openfoodfacts.net/api/v2/search?categories_tags_en={category}&fields=product_name,nutriscore_data,categories_tags,nutriscore_data'
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                liste_API_products = response.json().get('products', [])
            
            except requests.RequestException as e:
                self.stderr.write(self.style.ERROR(f"Error fetching data for category {category}: {e}"))
                continue

            for api_product in liste_API_products:
                nutri_score=api_product.get("nutriscore_data", {}).get("grade")
                if nutri_score:
                    product = Product(
                        name=api_product["product_name"],
                        nutri_score=nutri_score,
                        )
                    all_products.append(product)

            if all_products:
                Product.objects.bulk_create(all_products)
                all_products.clear()
                self.stdout.write(self.style.SUCCESS(f'  Enregistrement des produits pour la catégorie {category} : OK'))
            
        self.stdout.write(self.style.SUCCESS('Enregistrement des produits dans la Base de données : OK'))
