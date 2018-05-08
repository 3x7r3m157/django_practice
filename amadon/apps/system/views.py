from django.shortcuts import render, redirect

def index(request):
    request.session['total'] = 0
    return render(request, 'amadon/index.html')

def monkey(request):
    request.session['amount'] = request.POST['monkey']
    request.session['total'] += int(request.POST['monkey'])
    return redirect(thankyou)

def giraffe(request):
    request.session['amount'] = request.POST['giraffe']
    request.session['total'] += int(request.POST['giraffe'])
    return redirect(thankyou)

def elephant(request):
    request.session['amount'] = request.POST['elephant']
    request.session['total'] += int(request.POST['elephant'])
    return redirect(thankyou)

def thankyou(request):
    return render(request, 'amadon/thankyou.html')
