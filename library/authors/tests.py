from django.test import TestCase
from .models import Author
import datetime

# Suite de tests pour le modèle Author.
class AuthorModelTests(TestCase):
    # Configuration initiale pour les tests du modèle.
    def setUp(self):
        # Crée une instance de Author pour les tests.
        self.author = Author.objects.create(
            name="J.R.R. Tolkien",
            birth_date=datetime.date(1892, 1, 3),
            biography="A famous author of fantasy."
        )

    # Teste la création d'une instance de Author.
    def test_author_creation(self):
        self.assertIsInstance(self.author, Author)
        self.assertEqual(self.author.name, "J.R.R. Tolkien")
        # Vérifie la méthode __str__ de l'auteur.
        self.assertEqual(str(self.author), "J.R.R. Tolkien")

    # Teste les valeurs des champs de l'instance Author.
    def test_author_fields(self):
        self.assertEqual(self.author.birth_date, datetime.date(1892, 1, 3))
        self.assertEqual(self.author.biography, "A famous author of fantasy.")

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# Le modèle Author est déjà importé par AuthorModelTests.

# Suite de tests pour l'API des Authors.
class AuthorAPITests(APITestCase):
    # Configuration initiale pour les tests d'API.
    def setUp(self):
        # Crée des données et des instances d'auteurs pour les tests.
        self.author1_data = {"name": "George Orwell", "birth_date": "1903-06-25"}
        self.author1 = Author.objects.create(**self.author1_data)
        self.author2_data = {"name": "J.K. Rowling", "biography": "Author of Harry Potter"}
        self.author2 = Author.objects.create(**self.author2_data)

        # URLs pour les opérations API. 'author-list' et 'author-detail' sont les noms de base définis dans urls.py.
        self.list_url = reverse('author-list')
        self.detail_url = reverse('author-detail', kwargs={'pk': self.author1.pk})

    # Teste la récupération de la liste des auteurs.
    def test_get_author_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Vérifie que le nombre d'auteurs retournés est correct.
        self.assertEqual(len(response.data), 2)
        # Vérifie si le nom d'un des auteurs est présent dans la réponse.
        self.assertTrue(any(d['name'] == self.author1_data['name'] for d in response.data))

    # Teste la récupération du détail d'un auteur.
    def test_get_author_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.author1_data['name'])

    # Teste la création d'un nouvel auteur.
    def test_create_author(self):
        new_author_data = {"name": "Leo Tolstoy", "birth_date": "1828-09-09"}
        response = self.client.post(self.list_url, new_author_data, format='json')
        # Vérifie que la création a réussi (status HTTP 201).
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Vérifie que le nombre total d'auteurs a augmenté.
        self.assertEqual(Author.objects.count(), 3)
        self.assertEqual(response.data['name'], new_author_data['name'])

    # Teste la mise à jour d'un auteur existant.
    def test_update_author(self):
        updated_data = {"name": "Eric Arthur Blair", "birth_date": "1903-06-25", "biography": "Known as George Orwell"}
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Rafraîchit l'instance depuis la base de données pour vérifier les modifications.
        self.author1.refresh_from_db()
        self.assertEqual(self.author1.name, updated_data['name'])
        self.assertEqual(self.author1.biography, updated_data['biography'])

    # Teste la suppression d'un auteur.
    def test_delete_author(self):
        response = self.client.delete(self.detail_url)
        # Vérifie que la suppression a réussi (status HTTP 204).
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Vérifie que le nombre total d'auteurs a diminué.
        self.assertEqual(Author.objects.count(), 1)
        # Vérifie que l'auteur n'existe plus dans la base de données.
        self.assertFalse(Author.objects.filter(pk=self.author1.pk).exists())
