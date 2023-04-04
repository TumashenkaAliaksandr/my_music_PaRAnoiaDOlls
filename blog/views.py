from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog-full.html')

def single(request):
    return render(request, 'blog/single-full.html')
