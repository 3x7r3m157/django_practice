from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    request.session['data'] = {
        'casino': '',
        'house': '',
        'cave': '',
        'farm': '',
    }


    if 'activitystream' not in request.session:
        request.session['activitystream'] = []

    if 'total' not in request.session:
        request.session['total'] = 0


    return render(request, 'ninjagold/index.html', request.session['data'])

def processfarm(request):
    request.session['data']['farm'] = random.randint(10,21)
    request.session['winorlose'] = random.randint(0,2)
    print (request.session['activitystream'].reverse())


    if request.session['winorlose']  > 0:
        request.session['total'] += request.session['data']['farm']
        request.session['activitystream'].append('Found a treasure chest and earned {} gold from the farm!'.format(request.session['data']['farm']))

    if request.session['winorlose']  == 0:
        request.session['total'] -= request.session['data']['farm']
        request.session['activitystream'].append('Got jumped and lost {} gold from the farm. Sadface'.format(request.session['data']['farm']))

    return redirect(index)

def processcave(request):
    request.session['data']['cave'] = random.randint(10,21)
    request.session['winorlose'] = random.randint(0,2)
    print (request.session['activitystream'].reverse())


    if request.session['winorlose']  > 0:
        request.session['total'] += request.session['data']['cave']
        request.session['activitystream'].append('Found a treasure chest and earned {} gold from the cave!'.format(request.session['data']['cave']))

    if request.session['winorlose']  == 0:
        request.session['total'] -= request.session['data']['cave']
        request.session['activitystream'].append('Got jumped and lost {} gold from the cave. Sadface'.format(request.session['data']['cave']))

    return redirect(index)

def processhouse(request):
    request.session['data']['house'] = random.randint(10,21)
    request.session['winorlose'] = random.randint(0,2)
    print (request.session['activitystream'].reverse())


    if request.session['winorlose']  > 0:
        request.session['total'] += request.session['data']['house']
        request.session['activitystream'].append('Found a treasure chest and earned {} gold from the house!'.format(request.session['data']['house']))

    if request.session['winorlose']  == 0:
        request.session['total'] -= request.session['data']['house']
        request.session['activitystream'].append('Got jumped and lost {} gold from the house. Sadface'.format(request.session['data']['house']))

    return redirect(index)

def processcasino(request):
    request.session['data']['casino'] = random.randint(10,21)
    request.session['winorlose'] = random.randint(0,2)
    print (request.session['activitystream'].reverse())


    if request.session['winorlose']  > 0:
        request.session['total'] += request.session['data']['casino']
        request.session['activitystream'].append('Found a treasure chest and earned {} gold from the casino!'.format(request.session['data']['casino']))

    if request.session['winorlose']  == 0:
        request.session['total'] -= request.session['data']['casino']
        request.session['activitystream'].append('Got jumped and lost {} gold from the casino. Sadface'.format(request.session['data']['casino']))

    return redirect(index)
