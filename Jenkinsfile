pipeline {
    agent any
    stages {
        stage('Change Directory') {
            steps {
                sh 'cd /home/amaka013/Simple_Django_website'
            }
        }
	    stage('Enable virtual environment') {     
            steps {        
                sh 'source venv/bin/activate'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}
