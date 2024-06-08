pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                withCredentials([string(credentialsId: 'browserstack-credentials', variable: 'BROWSERSTACK_KEY')]) {
                    sh 'python3 -m venv bsenv'
                    sh '''
                    source bsenv/bin/activate
                    pip install -r requirements.txt
                    BROWSERSTACK_ACCESS_KEY=$BROWSERSTACK_KEY python3 scripts/parallel.py
                    '''
                }
            }
        }
    }
}
