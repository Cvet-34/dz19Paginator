from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

# Create your views here.


def news(request):
    news = News.objects.all().order_by('-date')
    page_news = request.GET.get('page_news', 5)
    paginator = Paginator(news, page_news)

    page_number = request.GET.get('page')   # запрос и информация от пользователя на какой стр находится
    page_obj = paginator.get_page(page_number)
    return render(request, "news.html", {'page_obj':page_obj})









