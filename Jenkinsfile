pipeline {
    agent any
    stages {
        stage('Change Directory') {
            steps {
		    script { dir ('/home/amaka013/Simple_Django_website')
			   }
            }
        }
	    stage('Enable virtual environment') {     
            steps {        
                sh 'source env/bin/activate'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}
