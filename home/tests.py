from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        """
        Testa se a página inicial está acessível (HTTP 200).
        """
        response = self.client.get(reverse('home'))  
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        """
        Testa se o conteúdo da página inicial contém a mensagem da pipeline.
        """
        response = self.client.get(reverse('home'))
        self.assertContains(response, "🚀 Pipeline Django Funcionando!")
