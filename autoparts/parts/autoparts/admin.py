from django.contrib import admin

from .models import Car, CategoryParts, SchemePart, Parts,Journal

admin.site.register(Car)
admin.site.register(CategoryParts)
admin.site.register(SchemePart)
admin.site.register(Parts)
admin.site.register(Journal)
