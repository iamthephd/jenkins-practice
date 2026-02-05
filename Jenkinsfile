pipeline {
    agent any
    stages {
        stage("Clean Up") {
            steps {
                echo "Cleaning up the workspace..."
                deleteDir()
            }
        }
        stage("Clone Repository") {
            steps {
                sh "git clone https://github.com/iamthephd/jenkins-practice.git"
            }
        }
        
        stage('Install Dependencies') {
            steps {
                dir('jenkins-practice') {
                sh '''
                uv venv
                source .venv/bin/activate
                uv pip install -r requirements.txt
                '''
                }
            }
        }

        stage('Start Application') {
            steps {
                dir('jenkins-practice') {
                sh '''
                source .venv/bin/activate
                python main.py &
                sleep 5
                '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('jenkins-practice') {
                sh '''
                source .venv/bin/activate
                python test.py
                '''
                }
            }
        }
        }
    }