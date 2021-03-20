pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'cd /home/amaka013/Simple_Django_website'
            }
        }
	    stage('Test on Linux') {     
            steps {        
                sh 'git fetch'
            }
        }
        stage('Test on Windows') {
            steps {
                sh 'git pull origin '
            }
        }
    }
}
