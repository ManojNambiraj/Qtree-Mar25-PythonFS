from django.shortcuts import render

datas = [
    {"id": 1, "title": "Post 1", "content": "card content post 1", "img": "https://image01-in.oneplus.net/media/202406/19/ec64eb41a8e787a798be1b71c13a51bb.png?x-amz-process=image/format,webp/quality,Q_80"},
    {"id": 2, "title": "Post 2", "content": "card content post 2"},
    {"id": 3, "title": "Post 3", "content": "card content post 3"},
    {"id": 4, "title": "Post 4", "content": "card content post 4"},
]

def index(request):
    return render(request, "index.html", {"datas": datas})

def detail(request, id):

    post = next(item for item in datas if item["id"] == id)

    return render(request, "detail.html", {"post": post})