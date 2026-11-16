from django.http import HttpResponse


def index(request):
    return HttpResponse("Да это же тот самый article")