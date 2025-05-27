from rest_framework import serializers
from .models import Author

# Serializer pour le modèle Author.
# Convertit les instances de Author en JSON et vice-versa.
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        # Modèle à sérialiser.
        model = Author
        # Champs à inclure dans la représentation sérialisée.
        fields = ['id', 'name', 'birth_date', 'biography']
