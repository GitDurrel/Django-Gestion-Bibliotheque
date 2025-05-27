# 📚 Projet de Gestion de Bibliothèque

## 🚀 Objectif  
Ce projet consiste à **développer une application web complète** avec Django permettant aux bibliothécaires de gérer leur **catalogue de livres**, ainsi que les **auteurs** et **emprunts des utilisateurs**.  
L’accent est mis sur la **qualité du code**, la **bonne structuration du projet**, et une **couverture des tests d’au moins 80%**.  

---

## 📌 Fonctionnalités requises  
✅ **Gestion des livres** → Ajout, modification et suppression 📖  
✅ **Gestion des auteurs** → Création, modification et suppression ✍️  
✅ **Gestion des emprunts** → Prêt et retour des livres 🔄  
✅ **Recherche avancée** → Filtrer les livres par **titre, auteur ou catégorie** 🔍  
✅ **Système de réservation** → Permettre aux utilisateurs de réserver des livres 📅  
✅ **API REST** → Exposer les données via des endpoints accessibles 🌐  

---

## 🛠 Technologies utilisées  
- 🖥 **Framework principal** : Django 4.2+  
- 🔗 **API REST** : Django REST Framework  
- 🧪 **Tests** : Pytest & pytest-cov  
- 🔄 **CI/CD** : GitHub Actions  
- 📖 **Documentation API** : drf-yasg (Swagger)  
- 🎨 **Interface utilisateur** (optionnelle) : Bootstrap / Material UI  

---

## ⚙️ Structure du projet  
📂 **`library/`** → Projet Django  
📂 **`library/books/`** → Application gérant les livres  
📂 **`library/authors/`** → Application pour les auteurs  
📂 **`library/loans/`** → Gestion des emprunts  
📂 **`library/tests/`** → Tests unitaires et d’intégration  
📄 **`requirements.txt`** → Liste des dépendances  
📄 **`README.md`** → Documentation complète  

---

## ✅ Étapes à suivre pour Jules  

### 1️⃣ **Création du projet Django** 🎯  
- Initialiser Django avec `django-admin startproject library`  
- Créer les applications `books`, `authors` et `loans`  
- Définir les **modèles Django** pour les livres, auteurs et emprunts  

### 2️⃣ **Implémentation des tests unitaires et d’intégration** 🧪  
**Tests unitaires à ajouter :**  
✔ Modèles (`Book`, `Author`, `Loan`) → Vérifier la structure et les relations  
✔ Formulaires Django → Validation correcte des données  
✔ Services métiers → Tester la logique métier  

**Tests d’intégration :**  
✔ **Cas d’usage complet** : Ajouter un livre, emprunt par un utilisateur, retour du livre  
✔ **Tests API** (`GET`, `POST`, `PUT`, `DELETE`) → Vérifier les réponses et formats  

### 3️⃣ **Documentation et bonnes pratiques** 📖  
- Ajouter **Swagger** (`drf-yasg`) pour une documentation interactive  
- Fournir **des docstrings claires** pour chaque classe et fonction  
- Écrire **un README détaillé** expliquant l’installation et l’utilisation du projet  

### 4️⃣ **Automatisation CI/CD** 🔄  
✅ Mettre en place **GitHub Actions** pour tester à chaque `push`  
✅ Ajouter **flake8** pour contrôler la qualité du code  
✅ Générer un **rapport de couverture (`pytest-cov`)**  

---

## 📦 Livrables attendus  
📌 **Code source complet** du projet GitHub  
📌 **Tests avec couverture ≥ 80%**  
📌 **README clair pour installer et exécuter l’application**  
📌 **Rapport de couverture des tests (`pytest-cov`)**  

---

## 📊 Barème de notation (20 points)  
- **8 pts** → Conception et structuration du projet 📁  
- **3 pts** → Fonctionnalités de gestion de bibliothèque 📚  
- **10 pts** → Qualité des tests (`pytest`, `coverage`) 🧪  
- **2 pts Bonus** → Interface utilisateur soignée + fonctionnalités supplémentaires 🎨  

---

**Jules, exécute ces étapes en suivant les directives ci-dessus ! 🚀**  
