pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Vérification des fichiers du projet...'
                // Affiche les fichiers pour être sûr que Jenkins les voit
                sh 'ls -la'
            }
        }

        stage('Build Image') {
            steps {
                echo 'Construction de l\'image Docker (Flask)...'
                // On crée l'image à partir de ton Dockerfile
                sh 'docker build -t mon-app-flask:latest .'
            }
        }

        stage('Security Scan (SAST)') {
            steps {
                echo 'Analyse du code Python avec Bandit...'
                /* IMPORTANT : On monte le dossier actuel $(pwd) dans le conteneur Bandit.
                   Bandit va lire le code et s'arrêter s'il trouve des failles.
                */
                sh 'docker run --rm -v $(pwd):/src pysec/bandit -r /src'
            }
        }

        stage('Deploy (Local)') {
            steps {
                echo 'Nettoyage des anciens conteneurs et lancement...'
                // Supprime l'ancien conteneur s'il existe pour éviter les conflits de port
                sh 'docker rm -f test-api || true'
                // Lance l'API sur le port 5005 de Windows
                sh 'docker run -d --name test-api -p 5005:5000 mon-app-flask:latest'
                echo 'Application disponible sur http://localhost:5005'
            }
        }
    }
}
