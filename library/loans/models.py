from django.db import models
from books.models import Book

# Modèle représentant un emprunt de livre.
class Loan(models.Model):
    # Livre qui est emprunté. Relation ForeignKey vers le modèle Book.
    # Si le livre est supprimé, les emprunts associés sont aussi supprimés.
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    # Identifiant de l'utilisateur qui a emprunté le livre (ex: email, nom d'utilisateur).
    user_identifier = models.CharField(max_length=100, help_text="Identifiant de l'utilisateur qui a emprunté le livre (ex: email ou nom d'utilisateur)")
    # Date à laquelle le livre a été emprunté. Auto-générée à la création.
    loan_date = models.DateField(auto_now_add=True, help_text="Date à laquelle le livre a été emprunté")
    # Date à laquelle le livre doit être retourné.
    due_date = models.DateField(help_text="Date à laquelle le livre doit être retourné")
    # Date à laquelle le livre a été effectivement retourné. Peut être nul si non retourné.
    return_date = models.DateField(null=True, blank=True, help_text="Date à laquelle le livre a été retourné")
    # Indique si l'emprunt est toujours actif (non retourné ou retourné en retard).
    # Par défaut, un nouvel emprunt est actif.
    is_active = models.BooleanField(default=True, help_text="L'emprunt est-il actuellement actif?")

    def __str__(self):
        # Représentation textuelle d'un emprunt.
        return f"[{self.book.title}] emprunté par [{self.user_identifier}]"
