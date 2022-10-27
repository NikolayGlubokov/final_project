from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import SchemePart, Parts, CategoryParts, Car, Journal
from .forms import JournalForm


@login_required(login_url='/users/login')
def index(request):
    return render(request, 'autoparts/index.html')


@login_required(login_url='/users/login')
def add(request, part_id):
    current_page = request.META.get('HTTP_REFERER')
    part = Parts.objects.get(id=part_id)
    if request.method == 'POST':
        print(request.POST['price'])
    Journal.objects.create(users=request.user, num_scheme=part.num_scheme,
                           num_parts=part.num_parts, articul=part.articul, name=part.name,
                           price=request.POST['price'])
    return redirect(current_page)


@login_required(login_url='/users/login')
def schemes(request, cat_id):
    car = Car.objects.all()
    user = request.user
    print(user.car_name)
    print(car == user.car_name)
    for i in car:
        print(i.name_car)
        print(i.id)
        if i.name_car == user.car_name:
            schem = SchemePart.objects.filter(category=cat_id, car = i.id )
    context = {'schem': schem}
    return render(request, 'autoparts/schemes.html', context)


@login_required(login_url='/users/login')
def parts(request, schem_id):
    schem = SchemePart.objects.get(id = schem_id)
    parts = Parts.objects.filter(num_scheme=schem_id)
    form = JournalForm()
    context = {'parts': parts, 'form': form, 'schem': schem}
    return render(request, 'autoparts/parts.html', context)


@login_required(login_url='/users/login')
def category(request):
    cat = CategoryParts.objects.all()
    context = {'cat': cat}
    return render(request, 'autoparts/category.html', context)
