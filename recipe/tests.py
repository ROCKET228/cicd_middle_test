from django.test import TestCase
from django.urls import reverse
from .models import Recipe


class MainViewTest(TestCase):
    def setUp(self):
        Recipe.objects.create(name='Recipe 1', ingredients='Ingredient 1')
        Recipe.objects.create(name='Recipe 2', ingredients='Ingredient 2')

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)  # Ensure the response is successful
        self.assertTemplateUsed(response, 'main.html')  # Ensure the correct template is used
        self.assertQuerysetEqual(response.context['recipes'], ['<Recipe: Recipe 1>', '<Recipe: Recipe 2>'])

