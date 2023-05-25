from django.shortcuts import render
from .models import Recipe


def main(requests):
    recipes = Recipe.objects.all()
    return render(requests, 'main.html', context={'recipes':recipes})



