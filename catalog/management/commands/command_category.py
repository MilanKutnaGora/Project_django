from django.core.management import BaseCommand

from catalog.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {
                "pk": 1,
                "name": "Лодки",
                "description": "Лодки ПВХ"
            },
            {
                "pk": 2,
                "name": "Удилища",
                "description": "Спининги, фидерные, карповые"
            },
            {
                "pk": 3,
                "name": "Катушки",
                "description": "Безынерционные, карповые, мультипликаторные"
            },
            {
                "pk": 4,
                "name": "Приманки",
                "description": "Воблеры, блесны, кастмастеры"
            },
            {
                "pk": 5,
                "name": "Снаряжение",
                "description": "Кресла, стулья, столы"
            }
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        # Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)