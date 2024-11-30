from django.shortcuts import render
from .forms import ColorTestForm
from .models import ColorType, StyleRecommendation 
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

def home(request):
    if request.method == 'POST':
        form = ColorTestForm(request.POST)
        if form.is_valid():
            # Простой пример логики для определения цветотипа
            score = 0
            if form.cleaned_data['question_1'] == '1':
                score += 1
            if form.cleaned_data['question_2'] == '1':
                score += 1

            if score == 2:
                color_type = ColorType.objects.get(name="Зима")
            else:
                color_type = ColorType.objects.get(name="Весна")

            recommendations = StyleRecommendation.objects.filter(color_type=color_type)
            return render(request, 'twinkle/result.html', {'color_type': color_type, 'recommendations': recommendations})

    else:
        form = ColorTestForm()
    return render(request, 'twinkle/color_test.html', {'form': form})
from .forms import ClothingItem
def wardrobe(request):
    clothing_items = ClothingItem.objects.all()
    if request.method == 'POST':
        # Логика для добавления одежды в гардероб
        pass
    return render(request, 'twinkle/wardrobe.html', {'clothing_items': clothing_items})
