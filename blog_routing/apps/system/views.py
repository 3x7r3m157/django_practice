from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'blogs/index.html')

def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect(index)

def show(request, blog_id):
    response = 'placeholder to display blog' + ' ' + blog_id
    return HttpResponse(response, blog_id)

def edit(request, blog_id):
    response = 'placeholder to edit blog' + ' ' + blog_id
    return HttpResponse(response, blog_id)

def destroy(request, blog_id):
    return redirect(index)
# Create your views here.
