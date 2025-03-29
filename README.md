# Jeu du Pendu en Python

## Description
Ce projet est une implémentation du jeu du **Pendu** en Python. Il permet de jouer seul en devinant un mot choisi aléatoirement à partir d'une liste de mots français stockée dans un fichier texte (`liste_francais_modifiee.txt`). Le joueur propose des lettres et tente de trouver le mot avant que le dessin du pendu ne soit complet.

Le programme est accompagné de tests unitaires pour certaines fonctions clés, exécutables grâce au module `doctest`.

---

## Fonctionnalités
- **Choix aléatoire d'un mot** dans un fichier texte contenant une liste de mots.
- **Gestion des accents et des caractères spéciaux**, avec formatage automatique en lettres majuscules sans accents.
- **Affichage dynamique de la figure du pendu** en fonction du nombre d'erreurs.
- **Système de validation des entrées** pour garantir que seules des lettres valides sont saisies.
- **Rejeu possible** après chaque partie.

---

## Prérequis
- Python 3.x installé.
- Un fichier `liste_francais_modifiee.txt` contenant une liste de mots français, chaque mot étant sur une nouvelle ligne.
- Aucun autre module externe n'est requis.

---

## Installation et exécution
1. **Clonez le projet** ou copiez le code dans un fichier Python.
2. **Ajoutez un fichier `liste_francais_modifiee.txt`** dans le même répertoire que le fichier Python. Ce fichier doit contenir une liste de mots français.
3. **Exécutez le script Python** en lançant la commande suivante depuis le terminal :
   ```bash
   python nom_du_fichier.py
   ```

---

## Instructions de jeu
1. Le jeu choisit un mot aléatoirement et affiche des tirets représentant les lettres à deviner.
2. Vous devez proposer une lettre latine non accentuée.
3. Chaque lettre correcte dévoile sa position dans le mot. Sinon, une partie de la figure du pendu apparaît.
4. Vous gagnez si vous devinez toutes les lettres avant que le pendu ne soit entièrement dessiné.
5. Après chaque manche, le jeu vous propose de rejouer ou de quitter.

---

## Structure du code
- **`choix_mot`** : Fonction qui sélectionne un mot aléatoire dans le fichier.
- **`formate_mot`** : Formatage d'un mot en majuscules sans accents.
- **`genere_tirets`** : Génère une chaîne avec des tirets pour les lettres non encore trouvées.
- **`compte_restantes`** : Compte le nombre de lettres restantes à deviner.
- **`affiche_pendu`** : Affiche la figure du pendu en fonction du nombre d'erreurs.
- **`demande_joueur_lettre`** : Gère la saisie et la validation des lettres par le joueur.
- **`une_manche`** : Lance une manche du jeu.
- **`presentation`** : Affiche l'écran d'accueil du jeu.
- **`main`** : Fonction principale permettant de rejouer plusieurs manches.

---

## Tests
Le code utilise des **doctests** pour vérifier la validité de certaines fonctions. Vous pouvez exécuter ces tests en lançant le script, qui les déclenchera automatiquement si des erreurs sont détectées :
```bash
python nom_du_fichier.py
```

---

## Personnalisation
- Vous pouvez modifier la liste des mots en mettant à jour le contenu du fichier `liste_francais_modifiee.txt`.
- Il est possible d'améliorer la figure du pendu ou de changer les règles de jeu en éditant les fonctions correspondantes dans le code Python.

---

## Auteurs
Projet pédagogique réalisé dans le cadre d'un cours de NSI (Numérique et Sciences Informatiques) pour l'année scolaire 2022-2023.# Pendu
