pipeline {
    agent any
    stages {
        stage('setup') {
            environment {
                BROWSERSTACK_USERNAME = 'cristiandiaz_6RkCu2'
                BROWSERSTACK_ACCESS_KEY = 'CK3UwX9mbZT9dz8tdi2X'
            }
            steps {
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
