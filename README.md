# Basic Docker Project

## Prérequis
- Docker installé
- Docker Compose installé (optionnel)

## Partie A : Création d'un Serveur HTTP Minimaliste avec Docker

### Contenu des différentes pages du projet

#### server.py
```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "<html><body><h1>Hello, Docker!</h1></body></html>"
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
```

#### Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app/server.py ./
CMD ["python", "server.py"]
```

#### docker-compose.yml
```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
```

### Exécution avec et sans Docker Compose

#### a) Sans Docker Compose

1. Construire l'image Docker :
```bash
docker build -t basic-docker-project .
```

2. Exécuter le conteneur :
```bash
docker run -p 8000:8000 --name docker-project-sans-compose basic-docker-project
```

#### b) Avec Docker Compose

1. Lancer le projet :
```bash
docker-compose up --build
```

#### c) Accès au site
Rendez-vous sur [http://localhost:8000](http://localhost:8000)

---

## Partie B : Pousser l'image de l'application vers DockerHub

### 1) Construire une image Docker de l'application
```bash
docker build -t moussasy23/basic-docker-project:latest .
```

### 2) Se connecter à DockerHub via la ligne de commande
```bash
docker login
```
> Suivez les instructions en ligne de commande, en utilisant le lien fourni et le code généré automatiquement.

### 3) Pousser l'image sur DockerHub
```bash
docker push moussasy23/basic-docker-project:latest
```
moussasy23 etant le nom de mon repository sur docker hub

### 4) Vérification
- Connectez-vous à [Docker Hub](https://hub.docker.com/)
- Vérifiez que l'image `basic-docker-project` est bien disponible.

---

## Pour télécharger et exécuter l'image depuis DockerHub

1. Télécharger l'image :
```bash
docker pull moussasy23/basic-docker-project:latest
```

2. Exécuter le conteneur :
```bash
docker run -p 8000:8000 moussasy23/basic-docker-project:latest
```


## Arrêter les conteneurs
```bash
docker-compose down
```

Ou, si lancé sans Docker Compose :
```bash
docker stop docker-project-sans-compose
```


## Convention de versionnement
- Utilisez des tags clairs comme `latest`, `v1.0`, `v2.0`, etc. pour suivre les différentes versions de l'image.

## CI/CD avec GitHub Actions

Ce projet utilise GitHub Actions pour automatiser la construction et le push de l'image Docker vers DockerHub.

### Fonctionnement du Pipeline
- Le pipeline s'exécute automatiquement après chaque push sur la branche `main`.
- Il construit l'image Docker et la pousse vers DockerHub sous le tag `latest`.

### Configuration
1. Les secrets `DOCKER_USERNAME` et `DOCKER_PASSWORD` doivent être ajoutés dans les secrets GitHub.
2. Le fichier de workflow est situé dans `.github/workflows/docker-publish.yml`.

### Vérification
- Vérifiez sur DockerHub que l'image `moussasy23/basic-docker-project` est bien mise à jour après un commit.
