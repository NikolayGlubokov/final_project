from django.shortcuts import render, redirect
from .models import SchemePart, Parts, CategoryParts, Car, Journal


def index(request):
    return render(request, 'autoparts/index.html')


def add(request, part_id):
    current_page = request.META.get('HTTP_REFERER')
    part = Parts.objects.get(id=part_id)
    print(request.user.id)
    Journal.objects.create(users=request.user, num_scheme=part.num_scheme,
                           num_parts=part.num_parts, articul=part.articul, name=part.name,
                           price=1000)
    return redirect(current_page)


def part(request, part_id):
    part = Parts.objects.get(pk=part_id)
    context = {'part': part}
    return render(request, 'autoparts/part.html', context)


def schemes(request, cat_id):
    schem = SchemePart.objects.filter(category=cat_id)
    print(schem)
    context = {'schem': schem}
    return render(request, 'autoparts/schemes.html', context)


def parts(request, schem_id):
    parts = Parts.objects.filter(num_scheme=schem_id)
    context = {'parts': parts}
    return render(request, 'autoparts/parts.html', context)


def category(request):
    cat = CategoryParts.objects.all()
    print(cat)
    context = {'cat': cat}
    return render(request, 'autoparts/category.html', context)
