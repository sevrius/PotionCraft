# PotionCraft

**PotionCraft** est un projet simple et amusant qui vous permet de gérer une liste de potions magiques. Vous pouvez ajouter, consulter et supprimer des potions via une interface web connectée à une API backend. Ce projet est entièrement containerisé avec Docker.

---

## Fonctionnalités principales
- Gérez une liste de potions magiques avec leurs noms, ingrédients et effets.
- Interface utilisateur simple (frontend) pour interagir avec les potions.
- API backend pour gérer les opérations CRUD (Create, Read, Delete).
- Architecture multi-service orchestrée avec Docker Compose.

---

## Structure du projet
Le projet est composé de deux services principaux :

### 1. **Service API Backend**
- **Description** : Une API REST construite avec Flask pour gérer les potions.
- **Port utilisé dans le container** : `80`
- **Endpoints principaux** :
  - `GET /potions` : Récupérer toutes les potions.
  - `POST /potions` : Ajouter une nouvelle potion.
  - `DELETE /potions/<id>` : Supprimer une potion par son ID.

### 2. **Service Frontend**
- **Description** : Une interface web simple construite avec HTML et JavaScript pour afficher et interagir avec les potions.
- **Port utilisé dans le container** : `80`
- **Fonctionnalités principales** :
  - Affichage de la liste des potions.
  - Ajout de nouvelles potions via un formulaire.
  - Suppression de potions existantes.

---

## Prérequis
- Docker et Docker Compose installés sur votre machine.

---

## Instructions d'installation et d'exécution

### 1. Clonez le dépôt
```bash
git clone <url-du-repo>
cd <nom-du-repo>
```

### 2. Compléter la configuration manquante
- Créer les Dockerfile
- Créer le docker-compose

### 3. Accédez aux services
- **Frontend** : [http://localhost:8080](http://localhost:8080)
- **API Backend** : [http://localhost:8081](http://localhost:8081)

---

## Utilisation

### Ajouter une potion
1. Remplissez le formulaire sur l'interface web.
2. Cliquez sur le bouton « Ajouter ».

### Supprimer une potion
1. Cliquez sur le bouton « Supprimer » associé à une potion dans l'interface web.

### Tester l'API directement
Utilisez un outil comme `curl` ou Postman pour interagir avec l'API :
```bash
# Exemple : Ajouter une potion
curl -X POST http://localhost:8081/potions \
    -H "Content-Type: application/json" \
    -d '{"name": "Potion d’invisibilité", "ingredients": ["Poudre de fée", "Eau de lune"], "effect": "Rend invisible pendant 10 minutes"}'
```

---

## Architecture technique
- **Backend** : Flask (Python), gère les requêtes REST.
- **Frontend** : HTML/CSS/JavaScript, affiche les potions et permet d’interagir avec l’API.
- **Orchestration** : Docker Compose pour orchestrer les deux services.
