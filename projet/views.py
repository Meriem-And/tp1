
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Kevin , this is my first page on Djando ")
