from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def content(request):
    return render(request, 'content.html')