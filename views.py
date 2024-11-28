from django.shortcuts import render
def index(request):
    return render(request, "main/index.html")
def autumn(request):
    return render(request, "main/autumn.html")
def colottype(request):
    return render(request, "main/colottype.html")
def log(request):
    return render(request, "main/log.html")
def razdeli(request):
    return render(request, "main/razdeli.html")
def spring(request):
    return render(request, "main/spring.html")
def summer(request):
    return render(request, "main/summer.html")
def winter(request):
    return render(request, "main/winter.html")