from rest_framework import serializers
from .models import Book

# Serializer pour le modèle Book.
# Gère la conversion des instances de Book en JSON et vice-versa.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # Modèle à utiliser pour la sérialisation.
        model = Book
        # Liste des champs du modèle à inclure dans la sortie sérialisée.
        # 'author' sera l'ID de l'auteur associé.
        fields = ['id', 'title', 'author', 'publication_date', 'isbn', 'category']
