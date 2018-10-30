from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def json(request):


    return HttpResponse("你好")


def index(request):
    context = {}
    article_list =[1,2,3]
    context['article_list'] = article_list
    return render(request, 'index.html', context)