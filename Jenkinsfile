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
                    sh "docker run -d --name simple-project-container -p 8080:8080 simple-project:latest"
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