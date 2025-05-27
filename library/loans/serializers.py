from rest_framework import serializers
from .models import Loan

# Serializer pour le modèle Loan.
# Transforme les instances de Loan en format JSON pour l'API et gère la validation des données entrantes.
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        # Spécifie le modèle sur lequel ce serializer est basé.
        model = Loan
        # Liste des champs à inclure dans la représentation sérialisée.
        # 'book' sera l'ID du livre associé.
        fields = ['id', 'book', 'user_identifier', 'loan_date', 'due_date', 'return_date', 'is_active']
        # Champs qui ne doivent pas être modifiables via l'API après la création.
        # 'loan_date' est défini automatiquement par `auto_now_add=True` dans le modèle.
        read_only_fields = ['loan_date']
