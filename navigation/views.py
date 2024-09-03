from django.shortcuts import render
import datetime


# Create your views here.
def about(request):

    return render(
        request,
        "navigation/about.html",
    )


def contact(request):
    return render(request, "navigation/contact.html")


def blog(request):
    d = {
        "author": "Rahim",
        "age": 23,
        "lst": ["python", "is", "best"],
        "birthday": datetime.datetime.now(),
        "val": "",
        "courses": [
            {
                "id": 1,
                "name": "Python",
                "fee": 5000,
                "description": "Python’s extensive standard library and vibrant community make it an excellent choice for both beginners and experienced developers.",
            },
            {
                "id": 2,
                "name": "Django",
                "fee": 10000,
                "description": "Django is a high-level Python web framework that simplifies building robust, scalable web applications.",
            },
            {
                "id": 3,
                "name": "C",
                "fee": 1000,
                "description": "C++ is a powerful, statically typed programming language known for its performance and versatility.",
            },
        ],
    }
    return render(request, "navigation/blog.html", d)
