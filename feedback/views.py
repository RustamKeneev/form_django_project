from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        if len(name) == 0 or len(name) > 20:
            return render(request,'feedback/feedback.html', context={'got_error': True})
        surname = request.POST['surname']
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html', context={'got_error': False})


def done(request):
    return render(request, 'feedback/done.html')