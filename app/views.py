from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted successfully')
        else:
            return HttpResponse('data is not valid')
    return render(request,'inserttopic.html',d)            