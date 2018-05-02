from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# from django.contrib.sessions import session
# Create your views here.
def index(request):
    count = request.session['count']
    context = {
        'randomword': get_random_string(length=32, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'),
        'randomwordblank': 'Please click to generate a random word',
        'count': count,
    }

    return render(request, 'randomword/index.html', context)

def generateWord(request):
    print ('hit generateWord')

    if request.POST['generate']:
        request.session['count'] += 1

    return redirect(index)

def resetWord(request):
    print ('hit resetWord')

    if request.POST['reset']:
        request.session['count'] = 0
        
    return redirect(index)
