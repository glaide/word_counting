
from .forms import FormText
from django.shortcuts import render


def text_box(request):
    message = ''
    form = FormText()
    if request.GET:
        if form.is_valid:
            text = request.GET['words']
            countOfWords = len(text.split())
            if countOfWords != 0:
                message = 'The total number of words is: ' + f'{countOfWords}'
       
    return render(request, "init.html",{"message" : message, "form": form})
