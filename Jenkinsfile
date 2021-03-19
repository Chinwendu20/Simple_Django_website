pipeline {
    agent any 
    stages {
        stage('Test') {
            steps {
                sh 'cd /home/amaka013/Simple_Django_website'
            }
	stage('Test') {
            steps {
                sh 'git fetch'
            }
	stage('Test') {
            steps {
                sh 'git pull'
            }
	stage('Test') {
            steps {
                sh 'source venv/Scripts/activate'
            }
	stage('Test') {
            steps {
                sh 'python3.9 manage.py test'
            }
	
            }
        }
    }
}