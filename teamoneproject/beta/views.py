from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def schoolIn(request):
    return render(request, 'schoolIn.html')

def schoolOut(request):
    return render(request, 'schoolOut.html')