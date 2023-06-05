pipeline {
  agent any
   stages {
       stage('setup') {
         steps {
             browserstack(credentialsId: 'browserstack-credentials') {
                 sh 'python3 -m venv bsenv'
                 sh '''
                 source bsenv/bin/activate
                 pip3 install -r requirements.txt
                 python3 scripts/parallel.py
                 '''
            }
         }
       }
     }
   }
