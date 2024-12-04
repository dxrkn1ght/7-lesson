from django.shortcuts import render, redirect
from .models import Car


def car_list(request):
    cars = Car.objects.all
    ctx = {'cars': cars}
    return render(request, 'cars/car_list.html', ctx)

def car_add(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    year = request.POST.get('year')

    if title and description :
        Car.objects.create(
            title=title,
            description=description,
            year=year
        )
        return redirect('cars:list')

    return render(request, 'cars/car_add.html')