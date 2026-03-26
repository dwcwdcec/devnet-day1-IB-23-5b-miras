pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Preparation stage'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage'
            }
        }

        stage('Results') {
            steps {
                echo 'Results stage'
            }
        }
    }
}
