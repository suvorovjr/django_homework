from django.core.management import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'title': 'Молочная продукция', 'description': 'Молоко'},
            {'title': 'Овоши', 'description': 'Только свежие овощи'},
            {'title': 'Фрукты', 'description': 'Свежие и сладкие фрукты'},
            {'title': 'Мясо', 'description': 'Любое мясо на выбор'},
            {'title': 'Бакалея', 'description': 'Круппы на любой вкус'},
            {'title': 'Приправы и соусы', 'description': 'Готовь вкуснее с нашими приправами'}
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)
