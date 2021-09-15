from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def rat(request):
    return render(request, 'home.html', {})

@csrf_exempt
def mode(request):
    fileList = request.POST
    print(fileList)
    return render(request, 'mode.html', {})

def selection(request):
    selection = request.GET.get('selection')
    return render(request, 'selection.html', {"selection": selection})