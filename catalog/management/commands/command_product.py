from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_list = [
            {
                "pk": 1,
                "name": "Лодка Хантер 320",
                "description": "Лодка ПВХ длина 3.2 м",
                "image": "",
                "category": Category.objects.get(pk=1),
                "price": 27000,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 2,
                "name": "Лодка Стелс 330",
                "description": "Лодка ПВХ длина 3.3 м",
                "image": "",
                "category": Category.objects.get(pk=1),
                "price": 29000,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 3,
                "name": "Лодка Сузумар 390",
                "description": "Лодка ПВХ длина 3.9 м",
                "image": "",
                "category": Category.objects.get(pk=1),
                "price": 49000,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 4,
                "name": "Спининг Кайда 2.7",
                "description": "Спининг длина 2.7 м",
                "image": "",
                "category": Category.objects.get(pk=2),
                "price": 2400,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 5,
                "name": "Фидер Крокодил 2.7",
                "description": "Фидер длина 2.7 м",
                "image": "",
                "category": Category.objects.get(pk=2),
                "price": 2800,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 6,
                "name": "Карповое удилище Осетр 2.7",
                "description": "Карповое удилище длина 2.7 м",
                "image": "",
                "category": Category.objects.get(pk=2),
                "price": 3600,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 7,
                "name": "Катушка Дайва",
                "description": "Катушка безынерционная",
                "image": "",
                "category": Category.objects.get(pk=3),
                "price": 5200,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 8,
                "name": "Катушка Салмо",
                "description": "Катушка карповая",
                "image": "",
                "category": Category.objects.get(pk=3),
                "price": 5800,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 9,
                "name": "Катушка Косадака",
                "description": "Катушка мультипликаторная",
                "image": "",
                "category": Category.objects.get(pk=3),
                "price": 9300,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 10,
                "name": "Воблер Рейд",
                "description": "Воблер 38 мм, 7г",
                "image": "",
                "category": Category.objects.get(pk=4),
                "price": 1400,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 11,
                "name": "Блесна Косадака",
                "description": "Блесна-цикада 21г",
                "image": "",
                "category": Category.objects.get(pk=4),
                "price": 300,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 12,
                "name": "Кастмастер Косадака",
                "description": "Блесна кастмастер 21г",
                "image": "",
                "category": Category.objects.get(pk=4),
                "price": 200,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 13,
                "name": "Кресло карповое",
                "description": "Складное, алюминевое",
                "image": "",
                "category": Category.objects.get(pk=5),
                "price": 17000,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 14,
                "name": "Стул",
                "description": "Стул-рюкзак",
                "image": "",
                "category": Category.objects.get(pk=5),
                "price": 1700,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            },
            {
                "pk": 15,
                "name": "Столик карповый",
                "description": "Складной, алюминевый",
                "image": "",
                "category": Category.objects.get(pk=5),
                "price": 10000,
                "date_base": "2020-01-01",
                "data_change": "2023-12-01"
            }
        ]
        products_for_create = []
        for product_item in products_list:
            products_for_create.append(Product(**product_item))

        Product.objects.all().delete()
        Product.objects.bulk_create(products_for_create)