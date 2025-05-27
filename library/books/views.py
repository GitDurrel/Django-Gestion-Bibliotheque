from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# ViewSet pour le modèle Book.
# Ce ViewSet gère les opérations CRUD standard pour les livres.
class BookViewSet(viewsets.ModelViewSet):
    # Ensemble de requête qui retourne tous les livres.
    # Peut être filtré ou ordonné ici si nécessaire.
    queryset = Book.objects.all()
    # Classe de serializer utilisée pour la validation et la sérialisation des données.
    serializer_class = BookSerializer
