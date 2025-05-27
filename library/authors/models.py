from django.db import models

# Modèle représentant un auteur de livres.
class Author(models.Model):
    # Nom complet de l'auteur.
    name = models.CharField(max_length=200, help_text="Entrez le nom de l'auteur")
    # Date de naissance de l'auteur, peut être nulle.
    birth_date = models.DateField(null=True, blank=True, help_text="Date de naissance de l'auteur")
    # Biographie de l'auteur, texte libre.
    biography = models.TextField(null=True, blank=True, help_text="Une brève biographie de l'auteur")

    def __str__(self):
        # Représentation textuelle de l'objet Author (utilisée dans l'admin, etc.).
        return self.name
