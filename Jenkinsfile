
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Starting Addition Project'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python monitoring.py'
            }
        }

        stage('Build Completed') {
            steps {
                echo 'Addition Project Build Successful!'
            }
        }
    }
}
