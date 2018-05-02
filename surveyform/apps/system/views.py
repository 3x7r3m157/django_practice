from django.shortcuts import render, redirect

# Create your views here.
def survey(request):
    return render(request, 'surveyform/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favorite'] = request.POST['favorite']
    request.session['comment'] = request.POST['comment']

    print (request.POST)
    return redirect(results)

def results(request):
    name = request.session['name']
    location = request.session['location']
    favorite = request.session['favorite']
    comment = request.session['comment']

    context = {
        'name': name,
        'location': location,
        'favorite': favorite,
        'comment': comment,
    }
    return render(request, 'surveyform/results.html', context)
