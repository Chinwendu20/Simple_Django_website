pipeline {
    agent any
    stages {
        stage('Change ') {
            steps {
		sh 'source /home/amaka013/Simple_Django_website/env/bin/activate'
		sh 'cd /home/amaka013/Simple_Django_website/'
		sh 'pwd'
		
            }
	}
	 stage('Change34 ') {
		 steps{
		 	script { dir ('/home/amaka013/Simple_Django_website/'){
		 	sh 'python manage.py test'
		 }
			       }
            }
	}
	
    }
}
