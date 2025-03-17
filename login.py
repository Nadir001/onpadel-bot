import requests
import os

# Récupérer les identifiants (passés en variables GitHub Actions)
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

session = requests.Session()

# 1️⃣ Vérifier l'email
email_check_url = "https://onpadel.gestion-sports.com/traitement/connexion.php"
email_data = {
    "ajax": "checkEmail",
    "email": email,
    "compte": "user"
}
session.post(email_check_url, data=email_data)

# 2️⃣ Connexion
login_data = {
    "ajax": "connexionUser",
    "id_club": "331",
    "email": email,
    "form_ajax": "1",
    "pass": password,
    "compte": "user",
    "playeridonesignal": "0",
    "identifiant": "identifiant",
    "externCo": "true"
}
session.post(email_check_url, data=login_data)

# 3️⃣ Accéder à l'espace membre
response = session.get("https://onpadel.gestion-sports.com/membre/")

print("[✅] Connexion réussie !")

