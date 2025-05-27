# 📚 Projet de Gestion de Bibliothèque (Système de Gestion de Bibliothèque)

Ce projet est une application web développée avec Django pour la gestion d'un catalogue de livres, d'auteurs et d'emprunts utilisateurs.

## ✨ Fonctionnalités Principales
- Gestion des livres (Ajout, modification, suppression)
- Gestion des auteurs (Création, modification, suppression)
- Gestion des emprunts (Prêt et retour des livres)
- API REST pour accéder et manipuler les données.
- Documentation interactive de l'API via Swagger.

## 🛠 Technologies Utilisées
- Framework principal : Django
- API REST : Django REST Framework
- Documentation API : drf-yasg (Swagger)
- Tests : Pytest & pytest-cov (utilisés pendant le développement)

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8+
- pip (Python package installer)
- Git

### 1. Cloner le Dépôt
```bash
git clone <URL_DU_DEPOT> # Remplacez <URL_DU_DEPOT> par l'URL réelle du dépôt
cd <NOM_DU_DOSSIER_PROJET> # Remplacez <NOM_DU_DOSSIER_PROJET> par le nom du dossier cloné
```

### 2. Créer un Environnement Virtuel (Recommandé)
```bash
python -m venv venv
```
Sous Windows :
```bash
venv\Scripts\activate
```
Sous macOS/Linux :
```bash
source venv/bin/activate
```

### 3. Installer les Dépendances
Assurez-vous que le fichier `requirements.txt` est présent à la racine du projet.
```bash
pip install -r requirements.txt
```

### 4. Configurer la Base de Données
Les migrations initiales créeront la base de données SQLite et les tables nécessaires.
```bash
python library/manage.py migrate
```
(Note: Si votre projet Django est imbriqué, par exemple `library/library/manage.py`, ajustez le chemin vers `manage.py` en conséquence. Le chemin actuel suppose que `manage.py` est dans un sous-dossier `library`.)

### 5. Créer un Superutilisateur
Pour accéder à l'interface d'administration de Django :
```bash
python library/manage.py createsuperuser
```
Suivez les instructions pour définir un nom d'utilisateur, une adresse e-mail et un mot de passe.

### 6. Lancer le Serveur de Développement
```bash
python library/manage.py runserver
```
L'application sera accessible à l'adresse `http://127.0.0.1:8000/`.

### 7. Accéder à l'API et à la Documentation
- **Interface d'administration Django** : `http://127.0.0.1:8000/admin/` (identifiants du superutilisateur requis)
- **Documentation API (Swagger)** : `http://127.0.0.1:8000/swagger/`
- **Documentation API (ReDoc)** : `http://127.0.0.1:8000/redoc/`
- Les endpoints de l'API sont disponibles sous `http://127.0.0.1:8000/api/` (par exemple, `/api/books/`, `/api/authors/`, `/api/loans/`).

## 🗣️ Langue
- La documentation de l'API (Swagger) est fournie en **français**.
- Les commentaires dans le code source sont également en **français**.

---
Ce README a été mis à jour pour refléter l'état actuel du projet et fournir des instructions claires pour son utilisation.
