from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer

# ViewSet pour le modèle Author.
# Fournit les actions CRUD (Create, Retrieve, Update, Delete) par défaut.
class AuthorViewSet(viewsets.ModelViewSet):
    # Requête de base pour récupérer tous les auteurs.
    queryset = Author.objects.all()
    # Classe de serializer à utiliser pour la conversion des données.
    serializer_class = AuthorSerializer
