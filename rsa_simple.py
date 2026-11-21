import requests
import random
from math import gcd

# Fonction qui détermine la primalité d'un nombre
def est_premier(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

# Génération d'un nombre premier aléatoire
def premier_aleatoire():
    while True:
        p = random.randint(1100, 9999)
        if est_premier(p):
            return p

# Génération des clés publiques et privées
def generer_cles():
    while True:
        # Génération de p et q
        p, q = premier_aleatoire(), premier_aleatoire()
        # Calcul de phi
        phi = (p - 1) * (q - 1)

        # Vérification si phi et e son premier entre eux avec e fixé a 65537
        if p != q and gcd(65537, phi) == 1:
            return p * q, 65537, pow(65537, -1, phi)   

# Fonction de chiffrement du message avec le text claire, n et e la clé publique du destinataire 
def chiffrer(texte, n, e):
    return [pow(ord(c), e, n) for c in texte]

# Fonction de dé chiffrement du message avec le text claire, n et  d la clé privée du destinataire 
def dechiffrer(nombres, n, d):
    return "".join(chr(pow(x, d, n)) for x in nombres)


def envoyer_via_telegram(message_chiffre):
    TOKEN = "8710232563:AAELgdicg1UygtdUJmux8w6dCFef54V_jYE"

    CHAT_ID = "-5306638153"
    
    # Transforme la liste de nombres chiffrés en texte séparé par des espaces
    texte_chiffre = "".join(map(str, message_chiffre))
    
    # URL de l'API Telegram
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # Données à envoyer
    payload = {
        "chat_id": CHAT_ID,
        "text": f" Message chiffré :\n{texte_chiffre}"
    }
    
    # Requête HTTP pour envoyer le message
    reponse = requests.post(url, json=payload)
    
    if reponse.status_code == 200:
        print("\n Message chiffré envoyé automatiquement sur Telegram !")
    else:
        print("\n Erreur lors de l'envoi :", reponse.text)

print("1 = creer mes cles | 2 = chiffrer un message | 3 = dechiffrer un message")
choix = input("Choix : ")

# Génération des clées
if choix == "1":
    n, e, d = generer_cles()

    # Ecriture de n et de la clée privé dans un cle_privee.txt
    open("cle_privee.txt", "w").write(f"{n} {d}")

    # Affichage clée publique (n, e)
    print(f"\nCLE PUBLIQUE (a envoyer) : n = {n}   e = {e}")
    print("Cle privee enregistree dans cle_privee.txt (ne la partagez JAMAIS)")

    # Préparation et envoi immédiat de la clé publique sur Telegram
    message_cle = f"Samuel : Voici clé publique RSA :\nn = {n}\ne = {e}"
    envoyer_via_telegram(message_cle)

# Chiffrement du message
elif choix == "2":

    # Récupération de la clée publique du destinataire  
    n, e = int(input("n du destinataire : ")), int(input("e du destinataire : "))

    # Application de fonction du chiffrement a partir du message entré
    resultat = chiffrer(input("Message de Samuel : "), n, e)
    print("\n Message chiffre (a envoyer) :\n" + " ".join(map(str, resultat)))

    # Envoi du message chiffré via la même logique 
    texte_chiffre = " ".join(map(str, resultat))
    envoyer_via_telegram(f"Samuel \n Message chiffré :\n{texte_chiffre}")
    
    print("\nMessage chiffre envoye !")

# Déchiffrement du message 
elif choix == "3":
    n, d = map(int, open("cle_privee.txt").read().split())
    nombres = [int(x) for x in input("Message chiffre : ").split()]
    print("\nMessage dechiffre :", dechiffrer(nombres, n, d))
