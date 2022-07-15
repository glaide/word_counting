
from .forms import FormText
from django.shortcuts import render


def text_box(request):
    message = 0
    form = FormText()

    if request.GET:
        
        text = request.GET['words']
        print(text)
        countOfWords = len(text.split())
        if countOfWords != 0:
            message = countOfWords
       
    return render(request, "init.html",{"message" : message, "form": form})
