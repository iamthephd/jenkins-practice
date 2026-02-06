pipeline {
    agent any

    environment {
        // Define your image name/tag here for easy updates
        IMAGE_NAME = "my-python-app"
        CONTAINER_NAME = "my-running-app"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Build Image") {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage("Run Container") {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    sh "docker run -d --rm --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:latest"
                }
            }
        }

        stage("Test") {
            steps {
                script {
                    sleep 10 // Wait for the container to start
                    sh "curl http://localhost:8000"
                    sh "docker stop ${CONTAINER_NAME}"
                    sh "docker rmi ${IMAGE_NAME}"
                }
            }
        }
    }
}