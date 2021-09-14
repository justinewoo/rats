from django.shortcuts import render

# Create your views here.
def rat(request):
    return render(request, 'home.html', {})