from django import forms
from recipe_box_v1.models import RecipeAuthor

class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
    # author = forms.ModelChoiceField(queryset=RecipeAuthor.objects.all())

class SudoRecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=RecipeAuthor.objects.all())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())