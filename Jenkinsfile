pipeline {
    agent any 
    stages {
        stage('Setup') {
            steps {
                script {
                    // Read secrets from the secrets.txt file
                    def secrets = readFile('secrets.txt').readLines().collect {
                        it.split('=').collect { it.trim() }
                    }
                    secrets.each { secret ->
                        environment[secret[0]] = secret[1]
                    }
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
