from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from books.models import Book # To check book state if necessary, though API checks are primary
from loans.models import Loan
import datetime
from django.utils import timezone

# Suite de tests d'intégration pour le cycle complet d'un emprunt.
class FullLoanCycleIntegrationTests(APITestCase):
    # Configuration initiale pour les tests d'intégration.
    def setUp(self):
        # URLs pour les appels API directs.
        self.authors_url = reverse('author-list')
        self.books_url = reverse('book-list')
        self.loans_url = reverse('loan-list')

    # Teste le cycle complet : création auteur, livre, emprunt, et retour du livre.
    def test_full_loan_and_return_cycle(self):
        # Étape 1: Créer un Auteur via l'API.
        author_data = {"name": "Auteur de Test Intégration", "birth_date": "1970-01-01"}
        response = self.client.post(self.authors_url, author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "La création de l'auteur a échoué.")
        author_id = response.data['id']
        self.assertIsNotNone(author_id, "L'ID de l'auteur ne devrait pas être nul.")

        # Étape 2: Créer un Livre par cet Auteur via l'API.
        book_data = {
            "title": "Le Livre de Test d'Intégration",
            "author": author_id, # Utilise l'ID de l'auteur créé précédemment.
            "publication_date": "2023-01-01",
            "isbn": "1234567890123", # ISBN unique pour le test.
            "category": "Tests"
        }
        response = self.client.post(self.books_url, book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "La création du livre a échoué.")
        book_id = response.data['id']
        self.assertIsNotNone(book_id, "L'ID du livre ne devrait pas être nul.")

        # Étape 3: Un utilisateur emprunte le Livre via l'API.
        due_date_str = (timezone.now().date() + datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        loan_data = {
            "book": book_id, # Utilise l'ID du livre créé.
            "user_identifier": "testeur_integration@example.com",
            "due_date": due_date_str
        }
        response = self.client.post(self.loans_url, loan_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "La création de l'emprunt a échoué.")
        loan_id = response.data['id']
        # Vérifie que l'emprunt est actif et non retourné initialement.
        self.assertTrue(response.data['is_active'], "L'emprunt devrait être actif à la création.")
        self.assertIsNone(response.data['return_date'], "La date de retour devrait être nulle à la création.")

        # Étape 4: L'utilisateur retourne le Livre. Mise à jour de l'emprunt via l'API.
        loan_detail_url = reverse('loan-detail', kwargs={'pk': loan_id})
        returned_date_str = timezone.now().date().strftime('%Y-%m-%d')
        
        # Pour une requête PUT, il est préférable de récupérer d'abord les données existantes
        # afin de s'assurer que tous les champs requis par le serializer sont présents.
        get_loan_response = self.client.get(loan_detail_url)
        self.assertEqual(get_loan_response.status_code, status.HTTP_200_OK, "La récupération de l'emprunt pour la mise à jour a échoué.")
        current_loan_data_for_put = get_loan_response.data 
        
        # Met à jour les champs pour le retour du livre.
        current_loan_data_for_put['return_date'] = returned_date_str
        current_loan_data_for_put['is_active'] = False
        # Assure que 'book' (ID) est bien présent, car c'est un champ du serializer.
        # current_loan_data_for_put['book'] = book_id # Redondant si 'book' est déjà l'ID dans la réponse GET.
        
        response = self.client.put(loan_detail_url, current_loan_data_for_put, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, "La mise à jour de l'emprunt (retour) a échoué.")
        # Vérifie que l'emprunt est maintenant inactif et que la date de retour est définie.
        self.assertFalse(response.data['is_active'], "L'emprunt devrait être inactif après le retour.")
        self.assertEqual(response.data['return_date'], returned_date_str, "La date de retour ne correspond pas.")

        # Étape 5: Vérifier le statut mis à jour de l'emprunt directement depuis la base de données.
        # C'est une vérification finale pour s'assurer de la persistance des données.
        updated_loan = Loan.objects.get(pk=loan_id)
        self.assertFalse(updated_loan.is_active, "L'emprunt devrait être inactif dans la BDD.")
        self.assertEqual(updated_loan.return_date.strftime('%Y-%m-%d'), returned_date_str, "La date de retour dans la BDD ne correspond pas.")
