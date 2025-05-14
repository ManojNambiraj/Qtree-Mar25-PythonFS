from typing import Any
from home.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args, **options):

        # Deleting the existing datas
        Category.objects.all().delete()
        
        categories = ["Sportz", "Music", "Drama", "Books", "Bikes", "Cars"]
            
        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))