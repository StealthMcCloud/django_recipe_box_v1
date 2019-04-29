from django.shortcuts import render
from recipe_box_v1.models import Recipe

def index(request):
    html = 'index.html'
    return render(request, html)

def recipe(request, recipe_id):
    print(recipe_id)
    recipe = Recipe.objects.filter(id=recipe_id)
    print(recipe)
    html = 'recipe.html'
    return render(request, html, {'recipe':recipe})

