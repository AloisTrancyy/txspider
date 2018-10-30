from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def index(request):
    context = {}
    article_list =[1,2,3]
    context['article_list'] = article_list
    return render(request, 'index.html', context)

def cbg_page(request):
    print(request)
    result = {}
    article_list =[1,2,3]

    result['article_list'] = article_list
    return render(request, 'index.html', result)

def delete_role(request):
    result = {}
    result['returncode'] = 0
    result['message'] = "this is message"
    result['result'] = [112,123,23]
    return HttpResponse(json.dumps(result), content_type="application/json")
