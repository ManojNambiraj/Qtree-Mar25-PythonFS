from django.shortcuts import render
import logging

datas = [
    {"id": 1, "title": "Post1",  "content": "Some quick example text for the post's content1.", "area":"Sportz", "size":20},
    {"id": 2, "title": "Post2",  "content": "Some quick example text for the post's content2.", "area":"Development"},
    {"id": 3, "title": "Post3",  "content": "Some quick example text for the post's content3.", "area":"Engineering"},
    {"id": 4, "title": "Post4",  "content": "Some quick example text for the post's content4.", "area":"Kids"},
]

def index(request):

    title = "Home Page"

    return render(request, "index.html", {'title': title, "datas": datas})

def details(request, id):
    
    post = next((item for item in datas if item["id"] == id), None)

    # logger = logging.getLogger("Testing")
    # logger.debug(post)

    return render(request, "detail.html", {"post": post})