from django.db import models
from authors.models import Author

# Modèle représentant un livre dans la bibliothèque.
class Book(models.Model):
    # Titre du livre.
    title = models.CharField(max_length=200, help_text="Entrez le titre du livre")
    # Clé étrangère liant le livre à son auteur.
    # Si un auteur est supprimé, ses livres sont également supprimés (CASCADE).
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    # Date de publication du livre.
    publication_date = models.DateField(null=True, blank=True, help_text="Date de publication du livre")
    # Numéro ISBN unique du livre (13 caractères).
    isbn = models.CharField(max_length=13, unique=True, help_text='Numéro ISBN à 13 caractères <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # Catégorie ou genre du livre.
    category = models.CharField(max_length=100, blank=True, help_text="Catégorie ou genre du livre")

    def __str__(self):
        # Représentation textuelle de l'objet Book.
        return self.title
