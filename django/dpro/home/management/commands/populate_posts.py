from typing import Any
from home.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args, **options):

        # Deleting the existing datas
        Post.objects.all().delete()
        
        titles = [
            "Post 1",
            "Post 2",
            "Post 3",
            "Post 4",
            "Post 5",
            "Post 5",
            "Post 6",
            "Post 7",
            "Post 8",
            "Post 9",
            "Post 10",
            "Post 11",
            "Post 12",
            "Post 13",
            "Post 14",
            "Post 15",
            "Post 16",
            "Post 17",
            "Post 18",
            "Post 19",
            "Post 20",
        ]

        contents = [
            "Content1 of the blog",
            "Content2 of the blog",
            "Content3 of the blog",
            "Content4 of the blog",
            "Content5 of the blog",
            "Content5 of the blog",
            "Content6 of the blog",
            "Content7 of the blog",
            "Content8 of the blog",
            "Content9 of the blog",
            "Content10 of the blog",
            "Content11 of the blog",
            "Content12 of the blog",
            "Content13 of the blog",
            "Content14 of the blog",
            "Content15 of the blog",
            "Content15 of the blog",
            "Content16 of the blog",
            "Content17 of the blog",
            "Content18 of the blog",
            "Content19 of the blog",
            "Content20 of the blog",
        ]

        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)


        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))