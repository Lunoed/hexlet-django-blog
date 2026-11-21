from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, **kwags):
        url = reverse("article", kwargs={"tags": "python", "article_id": 42})
        return redirect(url)



def about(request):
    return render(request, "about.html")