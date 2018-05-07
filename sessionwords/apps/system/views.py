from django.shortcuts import render, redirect
from time import gmtime, strftime

def process(request):
    request.session['formfunc'] = {
        'word': '',
        'color': '',
        'size': '',
        'time': '',
    }

    if not 'data' in request.session:
        request.session['data'] = []

    request.session['formfunc']['word'] = request.POST['word']
    request.session['formfunc']['color'] = request.POST['color']
    if request.session['formfunc']['size'] in request.session['formfunc']:
        request.session['formfunc']['size'] = 'big'
    if request.session['formfunc']['size'] not in request.session['formfunc']:
        request.session['formfunc']['size'] = 'normal'
    request.session['formfunc']['time'] = strftime("%b %d %Y %H:%M:%s", gmtime())

    request.session['data'].append(request.session['formfunc'])

    print (request.POST)
    print (request.session['data'])
    return redirect(index)

def index(request):
    return render(request, 'sessionwords/index.html')

def flush(request):
    request.session.flush()
    return redirect(index)
