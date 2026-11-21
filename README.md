# ProjetCrypto

Petit programme pedagogique en Python illustrant les bases du chiffrement RSA. Il permet de generer une paire de cles, de chiffrer un message caractere par caractere et de le dechiffrer avec la cle privee. Le script peut egalement envoyer les resultats via l'API Telegram.

> Ce projet utilise des nombres premiers volontairement petits et un chiffrement simple sans remplissage ni authentification. Il est destine a l'apprentissage et ne doit pas etre utilise pour proteger des informations sensibles.

## Prerequis

- Python 3
- Le paquet Python `requests`

Installation de la dependance :

```bash
pip install requests
```

## Utilisation

Depuis le dossier du projet :

```bash
python rsa_simple.py
```

Puis choisissez une action :

1. `1` : creer les cles publique et privee
2. `2` : chiffrer un message avec les cles publiques du destinataire
3. `3` : dechiffrer un message avec la cle privee locale

### Generer les cles

Lors du choix `1`, le programme affiche :

- `n` : composant de la cle publique
- `e` : exposant public, fixe a `65537`

La cle privee est enregistree dans `cle_privee.txt` sous la forme :

```text
n d
```

Partagez uniquement `n` et `e`. Ne partagez jamais `d` ni le contenu de `cle_privee.txt`.

### Chiffrer un message

Lors du choix `2`, renseignez la valeur `n` et l'exposant `e` du destinataire, puis saisissez le texte. Le programme affiche une suite d'entiers separes par des espaces.

Pour chiffrer `Bonjour` par exemple, le resultat aura cette forme :

```text
12345 67890 12345
```

Cette valeur exacte depend des cles generees.

### Dechiffrer un message

Lors du choix `3`, collez la suite d'entiers obtenue apres le chiffrement. Le programme lit `n` et `d` depuis `cle_privee.txt` puis affiche le texte original.

## Configuration Telegram

Les options de chiffrement envoient egalement les informations par Telegram avec `requests.post`.

Avant une utilisation reelle, remplacez les identifiants actuellement inscrits dans la fonction `envoyer_via_telegram()` par vos propres valeurs, ou mieux, chargez-les depuis des variables d'environnement. Ne placez jamais un jeton Telegram dans un depot public.

Si le depot ou les variables ont deja ete exposes, revisez immediatement le jeton Telegram concerne.

## Organisation des fichiers

- `rsa_simple.py` : generation des cles, chiffrement, dechiffrement et envoi Telegram
- `cle_privee.txt` : stock local de la cle privee
- `README.md` : documentation du projet

## Limites

- Les nombres premiers sont generes dans une petite plage aleatoire.
- Chaque caractere Unicode est chiffre separement avec son code numerique.
- Il n'y a pas de remplissage OAEP, de signature, ni de verification d'authenticite.
- Ce programme n'est pas adapte a un usage cryptographique professionnel.
