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
                sh "git clone "
            }

        }
    }
}