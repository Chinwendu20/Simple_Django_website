pipeline {
    agent any
    stages {
        stage('Change ') {
            steps {
		    script { dir ('/home/amaka013/Simple_Django_website'){
			    pwd
		    }
			    
			   }
            }
	}
	 stage('Test ') {
            steps {
			    sh 'source env/bin/activate'
			    sh 'python manage.py test'
		    }
			    
			   
            
        }
    }
}
