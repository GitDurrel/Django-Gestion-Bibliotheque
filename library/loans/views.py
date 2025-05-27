from rest_framework import viewsets
from .models import Loan
from .serializers import LoanSerializer

# ViewSet pour le modèle Loan.
# Fournit les opérations CRUD standard pour la gestion des emprunts.
class LoanViewSet(viewsets.ModelViewSet):
    # Requête de base pour lister tous les emprunts.
    # Des filtres peuvent être ajoutés ici, par exemple pour les emprunts actifs.
    queryset = Loan.objects.all()
    # Classe de serializer à utiliser pour la conversion des données d'emprunt.
    serializer_class = LoanSerializer

    # Des actions personnalisées pourraient être ajoutées ici, par exemple :
    # @action(detail=True, methods=['post'])
    # def return_book(self, request, pk=None):
    #     # Logique pour marquer un livre comme retourné.
    #     pass
