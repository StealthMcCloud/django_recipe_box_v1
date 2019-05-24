from django.shortcuts import render
from django.contrib.auth.models import User
from recipe_box_v1.models import Recipe
from recipe_box_v1.models import RecipeAuthor
from recipe_box_v1.forms import AuthorAddForm, RecipeAddForm

def index(request):
    recipes = Recipe.objects.all()
    html = 'index.html'
    return render(request, html, {'recipes':recipes})

def recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id)
    html = 'recipe.html'
    return render(request, html, {'recipe':recipe})

@login_required
def toggle_favorite_recipe_view(request, recipe_id):
    user_id = request.user.author.id
    user = Author.objects.filter(id=user_id).first()
    recipe = Recipe.objects.filter(id=recipe_id).first()
    if recipe in user.favorites.get_queryset():
        user.favorites.remove(recipe)
    else:
        user.favorites.add(recipe)
    return redirect('/content/' + str(recipe_id))

def author(request, author_id):
    author = RecipeAuthor.objects.filter(user_backend=author_id)
    recipes = Recipe.objects.filter(author_id=author_id)
    html = 'author.html'
    return render(request, html, {'author':author, 'recipes':recipes})

@login_required()
def add_recipe(request):
    html='add_recipe.html'
    form = None
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return render(request, 'addrecipesuccess.html')
    else:
        form = RecipeAddForm()
    return render(request, html, {'form': form})

@login_required()
def addedrecipe(request, recipeid):
    html = "add_recipe.html"
    form = None
    recipe = Recipe.objects.filter(id=recipeid)
    user_can_edit = can_user_edit_recipe(request,recipe[0])
    if not user_can_edit:
        return redirect('/') 
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.update(
                title=data["title"],
                description=data["description"],
                time_required=data["time_required"],
                instructions=data["instructions"]
            )
        return render(request, "addrecipesuccess.html")
    else:
        recipe_instance = recipe.first()
        data = {
            "title": recipe_instance.title,
            "description": recipe_instance.description,
            "time_required": recipe_instance.time_required,
            "instructions": recipe_instance.instructions,
        }
        form = AddRecipeForm(initial=data)
    return render(request, html, {"form": form})


def add_author(request):
    html='add_author.html'
    form = None
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data['name'],
            )
            RecipeAuthor.objects.create(
                name=data['name'],
                bio=data['bio'],
                user_backend=user
            )
            return render(request, 'addauthorsuccess.html')
    else:
        form = AuthorAddForm()
    return render(request,html,{'form': form})
