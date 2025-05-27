from django.test import TestCase
from .models import Loan
from books.models import Book
from authors.models import Author
import datetime
from django.utils import timezone # Utilisé pour calculer la date d'échéance.

# Tests pour le modèle Loan.
class LoanModelTests(TestCase):
    # Configuration exécutée avant chaque test du modèle d'emprunt.
    def setUp(self):
        # Crée un auteur et un livre pour les besoins du test d'emprunt.
        self.author = Author.objects.create(name="Aldous Huxley")
        self.book = Book.objects.create(
            title="Brave New World",
            author=self.author,
            isbn="9780060850524"
        )
        # Calcule une date d'échéance pour l'emprunt.
        self.due_date = timezone.now().date() + datetime.timedelta(days=14)
        # Crée une instance d'emprunt.
        self.loan = Loan.objects.create(
            book=self.book,
            user_identifier="testuser@example.com",
            due_date=self.due_date
        )

    # Teste la création d'un emprunt et sa représentation textuelle.
    def test_loan_creation(self):
        self.assertIsInstance(self.loan, Loan)
        self.assertEqual(self.loan.user_identifier, "testuser@example.com")
        # Vérifie que la date d'emprunt (auto_now_add) est définie.
        self.assertIsNotNone(self.loan.loan_date)
        # Vérifie la méthode __str__ (doit correspondre à la version française).
        expected_str = f"[{self.loan.book.title}] emprunté par [{self.loan.user_identifier}]"
        self.assertEqual(str(self.loan), expected_str)

    # Teste les valeurs par défaut d'un emprunt.
    def test_loan_default_values(self):
        # Un nouvel emprunt doit être actif par défaut.
        self.assertTrue(self.loan.is_active)
        # La date de retour doit être nulle par défaut.
        self.assertIsNone(self.loan.return_date)

    # Teste les relations de l'emprunt, notamment avec le livre.
    def test_loan_relationships(self):
        self.assertEqual(self.loan.book.title, "Brave New World")
        self.assertEqual(self.loan.book, self.book)

    # Teste les champs spécifiques de l'emprunt.
    def test_loan_fields(self):
        self.assertEqual(self.loan.due_date, self.due_date)

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# Les modèles Loan, Book, Author sont déjà importés.
# datetime et timezone sont également déjà importés.

import datetime # Assure l'importation de datetime pour strptime si ce n'est pas déjà fait plus haut.
from django.utils import timezone # Assure l'importation de timezone.

# Tests pour l'API des Loans (Emprunts).
class LoanAPITests(APITestCase):
    # Configuration exécutée avant chaque test d'API d'emprunt.
    def setUp(self):
        # Crée un auteur et un livre pour les tests d'API d'emprunt.
        self.author = Author.objects.create(name="F. Scott Fitzgerald")
        self.book = Book.objects.create(
            title="The Great Gatsby",
            author=self.author,
            isbn="9780743273565"
        )
        # Prépare les dates pour l'API (chaîne) et pour le modèle (objet date).
        self.due_date_str = (timezone.now().date() + datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        self.due_date_dt = datetime.datetime.strptime(self.due_date_str, '%Y-%m-%d').date()

        # Données pour créer un nouvel emprunt via l'API.
        self.loan_create_data = {
            "book": self.book.pk,
            "user_identifier": "reader@example.com",
            "due_date": self.due_date_str, # Utilise la date en format chaîne pour l'API.
        }
        # Crée une instance d'emprunt pour les tests GET, PUT, DELETE.
        self.loan1 = Loan.objects.create(
            book=self.book,
            user_identifier="another_reader@example.com",
            due_date=self.due_date_dt # Utilise l'objet date pour le modèle.
        )

        # URLs pour les opérations API sur les emprunts.
        self.list_url = reverse('loan-list')
        self.detail_url = reverse('loan-detail', kwargs={'pk': self.loan1.pk})

    # Teste la récupération de la liste des emprunts.
    def test_get_loan_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # Un seul emprunt créé dans setUp.
        self.assertEqual(response.data[0]['user_identifier'], self.loan1.user_identifier)

    # Teste la récupération du détail d'un emprunt.
    def test_get_loan_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_identifier'], self.loan1.user_identifier)

    # Teste la création d'un nouvel emprunt (prêt).
    def test_create_loan(self):
        response = self.client.post(self.list_url, self.loan_create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 2) # Vérifie l'augmentation du nombre d'emprunts.
        self.assertEqual(response.data['user_identifier'], self.loan_create_data['user_identifier'])
        # Vérifie que le nouvel emprunt est actif par défaut.
        self.assertTrue(response.data['is_active'])

    # Teste la mise à jour d'un emprunt pour simuler le retour d'un livre.
    def test_update_loan_return_book(self):
        # Simule le retour d'un livre en définissant la date de retour et en désactivant l'emprunt.
        returned_date_str = timezone.now().date().strftime('%Y-%m-%d')
        update_data = {
            "book": self.loan1.book.pk, # Champ requis par le serializer.
            "user_identifier": self.loan1.user_identifier, # Champ requis.
            "due_date": self.loan1.due_date.strftime('%Y-%m-%d'), # Champ requis.
            "return_date": returned_date_str,
            "is_active": False
        }
        response = self.client.put(self.detail_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.loan1.refresh_from_db() # Recharge l'objet depuis la DB.
        self.assertEqual(self.loan1.return_date.strftime('%Y-%m-%d'), returned_date_str)
        self.assertFalse(self.loan1.is_active)

    # Teste la suppression d'un emprunt.
    def test_delete_loan(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Loan.objects.count(), 0) # Vérifie que l'emprunt a été supprimé.
