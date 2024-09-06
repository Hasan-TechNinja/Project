from django.shortcuts import render

# Create your views here.


def Blogs(request):
    return render(request, 'blogs.html')