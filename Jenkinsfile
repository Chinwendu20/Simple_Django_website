pipeline {
    agent any
    stages {
        stage('Change Directory') {
            steps {
		    script { dir ('/home/amaka013/Simple_Django_website'){
			    sh 'source env/bin/activate'
			    sh 'python manage.py test'
		    }
			    
			   }
            }
        }
    }
}
