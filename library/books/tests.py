from django.test import TestCase
from .models import Book
from authors.models import Author # Import Author model
import datetime

# Suite de tests pour le modèle Book.
class BookModelTests(TestCase):
    # Prépare l'environnement pour chaque test de modèle.
    def setUp(self):
        # Crée un auteur pour associer aux livres.
        self.author = Author.objects.create(name="George Orwell")
        # Crée une instance de Book pour les tests.
        self.book = Book.objects.create(
            title="1984",
            author=self.author,
            publication_date=datetime.date(1949, 6, 8),
            isbn="9780451524935",
            category="Dystopian"
        )

    # Teste la création et la représentation textuelle d'un livre.
    def test_book_creation(self):
        self.assertIsInstance(self.book, Book)
        self.assertEqual(self.book.title, "1984")
        # Vérifie la méthode __str__ du livre.
        self.assertEqual(str(self.book), "1984")

    # Teste les relations du livre, notamment avec l'auteur.
    def test_book_relationships(self):
        self.assertEqual(self.book.author.name, "George Orwell")
        self.assertEqual(self.book.author, self.author)

    # Teste les valeurs des champs spécifiques du livre.
    def test_book_fields(self):
        self.assertEqual(self.book.publication_date, datetime.date(1949, 6, 8))
        self.assertEqual(self.book.isbn, "9780451524935")
        self.assertEqual(self.book.category, "Dystopian")

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# Les modèles Book et Author sont déjà importés par BookModelTests.
import datetime # Nécessaire pour la création de l'objet Book dans setUp pour APITestCase.

# Suite de tests pour l'API des Books.
class BookAPITests(APITestCase):
    # Prépare l'environnement pour chaque test d'API.
    def setUp(self):
        # Crée un auteur et un livre pour les tests d'API.
        self.author = Author.objects.create(name="Harper Lee")
        # Données pour la création du livre via l'API (utilise self.author.pk).
        self.book1_data_payload = {
            "title": "To Kill a Mockingbird",
            "author": self.author.pk,
            "publication_date": "1960-07-11",
            "isbn": "9780061120084",
            "category": "Southern Gothic"
        }
        # Instance de livre créée directement pour les tests GET, PUT, DELETE.
        self.book1 = Book.objects.create(
            author=self.author, # Instance d'auteur ici
            title="To Kill a Mockingbird", 
            publication_date=datetime.date(1960,7,11), 
            isbn="9780061120084", 
            category="Southern Gothic"
        )

        # URLs pour l'API des livres.
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # Teste la récupération de la liste des livres.
    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # Un seul livre créé dans setUp.
        self.assertEqual(response.data[0]['title'], self.book1.title)

    # Teste la récupération du détail d'un livre.
    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # Teste la création d'un nouveau livre via l'API.
    def test_create_book(self):
        new_book_data = {
            "title": "Go Set a Watchman",
            "author": self.author.pk, # Référence à l'ID de l'auteur.
            "publication_date": "2015-07-14",
            "isbn": "9780062409850",
            "category": "Novel"
        }
        response = self.client.post(self.list_url, new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2) # Vérifie l'augmentation du nombre de livres.
        self.assertEqual(response.data['title'], new_book_data['title'])

    # Teste la mise à jour d'un livre existant via l'API.
    def test_update_book(self):
        updated_data = {
            "title": "To Kill a Mockingbird (Revised)",
            "author": self.author.pk,
            "publication_date": "1960-07-11", # Doit être au format YYYY-MM-DD pour l'API.
            "isbn": "9780061120084", # L'ISBN reste le même.
            "category": "Classic" # Changement de catégorie.
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db() # Recharge l'objet depuis la DB.
        self.assertEqual(self.book1.title, updated_data['title'])
        self.assertEqual(self.book1.category, updated_data['category'])

    # Teste la suppression d'un livre via l'API.
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0) # Vérifie que le livre a été supprimé.
