from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class ArticlesView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Название приложения: article")

def index(request, tags: str, article_id: int):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}.")