from django.shortcuts import render

# Create your views here.
def index(request):

    title = "Home Page"

    datas = [
        {"id": 1, "title": "Post1",  "content": "Some quick example text for the post's content1.", "area":"Sportz"},
        {"id": 2, "title": "Post2",  "content": "Some quick example text for the post's content2.", "area":"Development"},
        {"id": 3, "title": "Post3",  "content": "Some quick example text for the post's content3.", "area":"Engineering"},
        {"id": 4, "title": "Post4",  "content": "Some quick example text for the post's content4.", "area":"Kids"},
    ]

    return render(request, "index.html", {'title': title, "datas": datas})

def details(request, id):
    return render(request, "detail.html", {"id": id})