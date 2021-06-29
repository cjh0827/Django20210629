from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Hello Django')


def test(request):
    return render(request, 'html/index.html')


def special_case_2021(request):
    return HttpResponse('special_case_2021')


def year_archive(request, year):
    return HttpResponse(f'year_archive:{year}')


def month_archive(request, year, month):
    return HttpResponse(f'month_archive:{year}:{month}')


def article_detail(request, year, month, slug):
    return HttpResponse(f'article_detail:{year}:{month}:{slug}')
