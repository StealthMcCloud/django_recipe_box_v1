# Generated by Django 2.2 on 2019-04-29 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe_box_v1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeauthor',
            name='id',
        ),
        migrations.AddField(
            model_name='recipeauthor',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipeauthor',
            name='user_backend',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('time_required', models.CharField(max_length=50)),
                ('instructions', models.TextField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_box_v1.RecipeAuthor')),
            ],
        ),
    ]