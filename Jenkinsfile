pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                browserstack(credentialsId: '45e840c5-54aa-4d7b-a2c5-03c10be01aff') {
                    sh 'python3 -m venv bsenv'
                    sh '''
                    source bsenv/bin/activate
                    pip install -r requirements.txt
                    python3 scripts/parallel.py
                    '''
                }
            }
        }
    }
}
