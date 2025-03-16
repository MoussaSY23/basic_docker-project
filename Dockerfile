# Utilisation de l'image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le container
COPY . /app


# Exposer le port que l'application va utiliser
EXPOSE 5000

# Définir la commande à exécuter lorsque le container est lancé
CMD ["python", "app.py"]
