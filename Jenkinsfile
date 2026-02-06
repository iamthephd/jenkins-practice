pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Build Image") {
            steps {
                script {
                    sh "docker build -t simple-project:latest ."
                }
            }
        }

        stage("Run Container") {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh "docker stop simple-project-container || true"
                    sh "docker rm simple-project-container || true"
                    sh "docker run -d --name simple-project-container -p 8000:8000 simple-project:latest"
                }
            }
        }

        stage("Test") {
            steps {
                script {
                    sh "curl http://localhost:8080"
                }
            }
        }
    }
}