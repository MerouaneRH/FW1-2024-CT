# Gestion de Catalogue de Formations Universitaires 🎓

Ce projet est une application web développée avec **Django** pour la gestion des formations et des unités d'enseignement (UE) d'un département universitaire. Il permet de consulter, ajouter, modifier et supprimer des formations et des UE, avec des fonctionnalités d'authentification et de gestion des autorisations.

---

## Fonctionnalités 🚀

- **Gestion des Formations** : Ajout, modification, suppression et consultation des formations.
- **Gestion des UE** : Ajout, modification, suppression et consultation des unités d'enseignement.
- **Authentification** : Connexion et déconnexion des utilisateurs.
- **Gestion des Autorisations** :
  - Les responsables de formation peuvent gérer les UE rattachées à leur formation.
  - Les responsables d'UE peuvent modifier les UE dont ils sont responsables.
- **Interface Utilisateur** : Améliorée avec **Bootstrap** pour une meilleure expérience utilisateur.

---

## Structure du Projet 🗂️

- **ct** : Projet Django principal.
- **uo** : Application Django pour la gestion des formations et des UE.
- **README.md** : Fichier contenant les informations sur le projet et les commandes utilisées.
- **ct/**, **uo/**, **manage.py** : Structure de base du projet Django.

---

## Installation et Utilisation 🛠️

### Prérequis

- **Python**
- **Django**
- **Docker**

### Commandes Utiles

1. **Lancer le conteneur Docker** :
   ```bash
   USERNAME=$(id -un) USERID=$(id -u) docker-compose up -d
   ```

2. **Vérifier l'utilisateur dans le conteneur** :
   ```bash
   docker exec -ti fw1-ct-votre_nom_utilisateur whoami
   ```

3. **Créer les migrations** :
   ```bash
   python manage.py makemigrations
   ```

4. **Appliquer les migrations** :
   ```bash
   python manage.py migrate
   ```

5. **Charger les données des enseignants** :
   ```bash
   python manage.py loaddata uo/fixtures/enseignant.json
   ```

6. **Charger les données des formations** :
   ```bash
   python manage.py loaddata uo/fixtures/formation.json
   ```

7. **Charger les données des UE** :
   ```bash
   python manage.py loaddata uo/fixtures/ue.json
   ```
   
---


## Équipe 👥

- **GUILLARD Joan**
- **HAMZE Muhamad**
- **TOUBAL Rabah**
- **RAHMOUN Merouane**
