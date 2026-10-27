pipeline {
    agent any
    stages {
        stage('Get Code') {
            steps {
                checkout scm
            }
        }
        stage('Install Tools') {
            steps {
                bat 'python -m pip install pytest'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest -v'
            }
        }
        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }
    }
}
