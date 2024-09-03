from django.shortcuts import render
import datetime


# Create your views here.
def about(request):
    d = {
        "author": "Rahim",
        "age": 23,
        "lst": ["python", "is", "best"],
        "birthday": datetime.datetime.now(),
        "val": "",
        "courses": [
            {"id": 1, "name": "Python", "fee": 5000},
            {"id": 2, "name": "Django", "fee": 10000},
            {"id": 3, "name": "C", "fee": 1000},
        ],
    }
    return render(request, "navigation/about.html", d)


def contact(request):
    return render(request, "navigation/contact.html")
